import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import subprocess
from MFRC522_python.mfrc522 import SimpleMFRC522
import datetime
import requests
from pprint import pprint
import sys
import time
import json

import jwt
import paho.mqtt.client as mqtt
import random
import cv2
#GPIO.setwarnings(False) #Ignore warning for now

ssl_private_key_filepath = '/home/pi/Semana-IoT-AIG/demo_private.pem'
ssl_algorithm = 'RS256'  # Either RS256 or ES256
root_cert_filepath = '/home/pi/Semana-IoT-AIG/roots.pem'
project_id = 'semana-i-aig'
gcp_location = 'us-central1'
registry_id = 'semana-i'
device_id = 'rasi'

cur_time = datetime.datetime.utcnow()


adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
adc.start_adc(0, gain=GAIN)

sensor_magnetico=29
GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BOARD) #Use physical pin number
GPIO.setup(sensor_magnetico, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
detect_flag=0
reader = SimpleMFRC522()
#print('Reading ADS1x15 values, press Ctrl-C to quit...')
#print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
#print('-' * 37)
#start = time.time()
#sensors = [0]*4
def create_jwt():
    token = {
        'iat': cur_time,
        'exp': cur_time + datetime.timedelta(minutes=60),
        'aud': project_id
    }

    with open(ssl_private_key_filepath, 'r') as f:
        private_key = f.read()

    return jwt.encode(token, private_key, ssl_algorithm)


_CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(
    project_id, gcp_location, registry_id, device_id)
_MQTT_TOPIC = '/devices/{}/events'.format(device_id)

client = mqtt.Client(client_id=_CLIENT_ID)
# authorization is handled purely with JWT, no user/pass, so username can be whatever
client.username_pw_set(
    username='unused',
    password=create_jwt())


def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))


def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')

client.on_connect = on_connect
client.on_publish = on_publish

# Replace this with 3rd party cert if that was used when creating registry
client.tls_set(ca_certs=root_cert_filepath)
client.connect('mqtt.googleapis.com', 443)
client.loop_start()

def read_adc():
    for i in range(4):
        sensors[i] = adc.read_adc(i, gain=GAIN)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*sensors))
    if sensors[0]>1000:
        callbackCamera()

def detect_face(detection_type):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    cnt_caras=0
    cnt=0
    cntz=0
    cnt_caras_anterior=0
    detect_flag=0
    while GPIO.input(sensor_magnetico) == GPIO.HIGH:
        cnt_caras=0
        ret,img=cap.read()
        if cap.isOpened()==True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
             #   cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cnt_caras=cnt_caras+1
            print(cnt_caras," faces detected")
            cv2.imshow('img', img)
            cv2.waitKey(1)
            if cnt_caras==cnt_caras_anterior and cnt_caras!=0:
                cnt+=1
            else:
                cnt=0
                cnt_caras_anterior=cnt_caras
                cntz+=1
            if cnt>8:
                cntz=0
            if (detection_type==0 and cnt>3) or (detection_type==1 and cntz>10):
                detect_flag=1
                break
    
    if GPIO.input(sensor_magnetico) == GPIO.HIGH:
        cv2.imwrite("/home/pi/Semana-IoT-AIG/last_image.png",img)
    cap.release()
    return detect_flag

age=[]
gender=[]
def callbackCamera(detect_flag):
    #subprocess.call(['fswebcam /home/pi/Semana-IoT-AIG/last_image.png', '-1'], shell=True)
    if detect_flag==1:
        face_uri = "https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&language=en"
        pathToFileInDisk = r'/home/pi/Semana-IoT-AIG/last_image.png'
        with open( pathToFileInDisk, 'rb' ) as f:
            data = f.read()
        print("Connecting to Azure")
        headers = { "Content-Type": "application/octet-stream" ,'Ocp-Apim-Subscription-Key': '7e9cfbb244204fb994babd6111235269'}
        response = requests.post(face_uri, headers=headers, data=data)
        faces = response.json()
        for value in faces['faces']:
            age.append(value['age'])
            gender.append(value['gender'])
        if(len(age)==0):
            text="Unknown"
            age.append(text)
            gender.append(text)
        for i in range(0,len(age)):
            print(age[i]," ", gender[i])
        detect_flag=0
        
        
def read_rfid():
    read_once_flag=True
    id_lista=[]
    text_lista=[]
    flag=1
    while(GPIO.input(sensor_magnetico) == GPIO.LOW and flag==1):
        try:
            id,text = reader.read_special()
            
        finally:
             cv2.waitKey(1)
        if(id!=None):
            flag=0
    if(flag==0):
        id_lista.append(id)
        text_lista.append(text)
    while(GPIO.input(sensor_magnetico) == GPIO.LOW):
        check=0
        id, text = reader.read_special()
        if(text!=None):
            for x in id_lista:
                if id==x:
                    check+=1
            if check<1:
                id_lista.append(id)
                text_lista.append(text)
        else: break
    return id_lista,text_lista


inv={'109913285498':"sprite_355",'385338090172':"sprite_355",'139867904941':"ades_durazno_200",'728886191288':"ades_durazno_200"}
total=0
for value in inv.values():
    total+=1
n=[0]*total
N=[1,1,1,1]
def inventory_change(n):
    while(GPIO.input(sensor_magnetico) == GPIO.LOW):
        id_lista,text_lista=read_rfid()
        #print("Esta es lal lista   ",id_lista)
        cnt=0
        for m in id_lista:
            cnt=0
            registrado=0
            for k in inv:
                #print(f"'{m}'","   ",f"'{k}'")
                if m==int(k):
                    print("Success")
                    n[cnt]+=1
                    registrado=1
                    break
                cnt+=1
            if(registrado!=1):
                print("Producto no registrado")
        #print(n)
        #print(registrado)
    return n

def gcs():   
             payload = '{{ "ts": {}, "age": "{}", "gender": "{}" , "num_of_products": {} , "products": "{}" }}'.format(int(time.time()), str(age[0]), gender[0],num_prod, str(prod[0]))
             print(payload)
#             client.publish(_MQTT_TOPIC, payload, qos=1)
             print("client.on_publish")
             time.sleep(1)

detection_type=0
print(N)
while True:
    num_prod=0
    l=[]
    prod=[]
    age=[]
    gender=[]
    n=[0]*total
    detection_type=0
    detect_flag=0
    detect_flag=detect_face(detection_type)
    callbackCamera(detect_flag)
    detection_type=1
    detect_flag=detect_face(detection_type)

    n=inventory_change(n)
    for i in range(0,len(n)):
#         print(n[i],"   ", (-1)**n[i])
        if((-1)**n[i]<0):
            N[i]=0
            num_prod+=1
            for value in inv.values():
                l.append(value)
            prod.append(l[i])
            #print(N[i])
#     print(N)
    print("Products  ",prod)
    gcs()
    
    #print(len(age))
    
    time.sleep(1)

client.loop_stop()
#     id_lista,text_lista=read_rfid()
#     print("****************")
#     for i in range(0, len(id_lista)-1,1):
#         print(id_lista[i],"  ",text_lista[i])
#     print("****************")
#     if GPIO.input(sensor_magnetico) == GPIO.HIGH:
#         print("1")
#     else: print("0")
#     time.sleep(1)
#    if (time.time() - start) >= 2.0:
#        start = time.time()
#        read_adc()
#    time.sleep(0.5)

#adc.stop_adc()