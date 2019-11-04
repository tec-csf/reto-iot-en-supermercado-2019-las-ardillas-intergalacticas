import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1

adc.start_adc(0, gain=GAIN)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

start = time.time()
values = [0]*4

while True:

    if (time.time() - start) >= 2.0:
        start = time.time()
        for i in range(4):
            values[i] = adc.read_adc(i, gain=GAIN)
    
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        
    time.sleep(0.5)

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc.stop_adc()
