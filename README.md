# IoT en el Supermercado
---
#### Equipo *[Poner aquí nombre del equipo]*

##### Integrantes:
1. *[Poner aquí Nombre y Apellidos del integrante 1]* - *[Poner aquí su Matrícula]* - *[Poner aquí su campus]*
2. *[Poner aquí Nombre y Apellidos del integrante 2]* - *[Poner aquí su Matrícula]* - *[Poner aquí su campus]*
3. *[Poner aquí Nombre y Apellidos del integrante 3]* - *[Poner aquí su Matrícula]* - *[Poner aquí su campus]*
4. *[Poner aquí Nombre y Apellidos del integrante 4]* - *[Poner aquí su Matrícula]* - *[Poner aquí su campus]*
5. *[Poner aquí Nombre y Apellidos del integrante 5]* - *[Poner aquí su Matrícula]* - *[Poner aquí su campus]*

---
## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* Todo el código de la solución debe estar desarrollado en Python 3.7 utilizando módulos y Programación Orientada a Objetos.
* Las lecturas de los sensores debe programarse de manera asíncrona.
* Todo el código debe incluir el manejo de excepciones y validación de errores.
* El equipo tiene la libertad de elegir los servicios cognitivos y de nube que desee utilizar, sin embargo, debe tener presente que la solución final se deberá ejecutar en una Raspberry Pi y en una de las siguientes plataformas en la nube: [Amazon Web Services](https://aws.amazon.com/), [Google Cloud Platform](https://cloud.google.com/?hl=es) o [Microsoft Azure](https://azure.microsoft.com/es-mx/).
* El proyecto debe utilizar algunos de los servicios de reconocimiento de imágenes como: [Azure Computer Vision API](https://azure.microsoft.com/es-mx/services/cognitive-services/computer-vision/), [Google Vision AI](https://cloud.google.com/vision/), [Amazon Rekognition](https://aws.amazon.com/rekognition/).
* El proyecto debe utilizar algún servicio de IoT en la nube como: [Azure IoT Hub](https://azure.microsoft.com/es-mx/services/iot-hub/), [Google IoT Core](https://cloud.google.com/iot-core/?hl=es), [Amazon IoT Core](https://aws.amazon.com/es/iot-core/).
* Para la ingesta de datos, se debe utilizar un servicio de mensajería asíncrono como [Azure Service Bus](https://azure.microsoft.com/es-mx/services/service-bus/), [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/?hl=es-419), [Amazon SNS](https://aws.amazon.com/sns/).
* Para el procesamiento de los paquetes de IoT se debe utilizar un servicio como [Azure Functions](https://azure.microsoft.com/es-mx/services/functions/), [Cloud Functions](https://cloud.google.com/functions/), [Amazon Lambda](https://aws.amazon.com/lambda/).
* Para el almacenamiento de la información se debe utilizar un servicio como [Azure SQL Datawarehouse](https://azure.microsoft.com/es-mx/services/sql-data-warehouse/), [Google BigQuery](https://cloud.google.com/bigquery/?hl=es), [Amazon Redshift](https://aws.amazon.com/es/redshift/).
Para la visualización de los datos se debe utilizar un servicio como [Azure Power BI](https://powerbi.microsoft.com/es-es/), [Google Data Studio](https://datastudio.google.com), [Amazon Quicksight](https://aws.amazon.com/quicksight/).
* La conexión entre la Raspberry Pi y el servicio de nube de IoT debe realizarse utilizando el protocolo MQTT y llaves criptográficas para la autenticación.
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomendamos la lectura [*Microservices*](https://martinfowler.com/articles/microservices.html) de [Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Los diferentes componentes del proyecto (*frontend*, *backend*, *API RESTful*, bases de datos, entre otros) pueden ejecutarse, opcionalmente, sobre contenedores [Docker](https://www.docker.com/) y utilizar [Kubernetes](https://kubernetes.io/) como orquestador.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en este repositorio de GitHub. Favor de mantener la estructura de carpetas generada.

### 1.2 Estructura del repositorio
El proyecto debe seguir la siguiente estructura de carpetas, la cual generamos por usted:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app, dashboards, etc.)
    - backend			# Carpeta con la solución del backend (CMS, API, Funciones, etc.)
    - sensors           # Carpeta con los códigos que se ejecutan en el RPi
    - datasets		        # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - docs			# Carpeta con la documentación del proyecto
```

### 1.3 Documentación  del reto

Como parte de la entrega final del reto, se debe incluir la siguiente información:

* Justificación del modelo o servicio de *Machine Learning* que seleccionaron.
* Descripción del o los *datasets* y las fuentes de información utilizadas.
* Guía de configuración, instalación y despliegue de la solución tanto en la Raspberry Pi como en la plataforma en la nube  seleccionada.
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

*[Incluya aquí la descripción del proyecto seleccionado.]*

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.

### 3.1 Modelos o servicios de *Machine Learning* utilizados

*[Incluya aquí una explicación del análisis realizado y la justificación de los modelos y/o servicios de *Machine Learning* seleccionados. Incluya todo lo que considere necesario para que una persona sin conocimientos técnicos pueda entender de que trata su solución.]*

### 3.2 Arquitectura de la solución

*[Incluya aquí un diagrama donde se aprecie la arquitectura de la solución implementada, así como la interacción entre los diferentes componentes de la misma.]*

*[Incluya imágenes del circuito armado con los sensores conectados.]*

### 3.3 Frontend

*[Incluya aquí una explicación de la solución utilizada para el frontend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.3.1 Lenguaje de programación
#### 3.3.2 Framework
#### 3.3.3 Librerías de funciones o dependencias

### 3.4 Backend

*[Incluya aquí una explicación de la solución utilizada para el backend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.4.1 Lenguaje de programación
#### 3.4.2 Framework
#### 3.4.3 Librerías de funciones o dependencias

*[Incluya aquí una explicación de cada uno de los endpoints que forman parte de la API. Cada endpoint debe estar correctamente documentado.]*

*[Por cada endpoint debe incluir lo siguiente:]*

* **Descripción**:
* **URL**:
* **Verbos HTTP**:
* **Headers**:
* **Formato JSON del cuerpo de la solicitud**: 
* **Formato JSON de la respuesta**:

### 3.5 Sensores

*[Incluya aquí una explicación de la solución utilizada para implementar la captura de datos de los diferentes sensores en la Raspberry Pi. No olvide incluir las ligas o referencias donde se puede encontrar información de los sensores, lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.5.1 Lenguaje de programación
#### 3.5.2 Framework
#### 3.5.3 Librerías de funciones o dependencias

## 3.6 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación de este repositorio hasta el despliegue de la solución en una Raspberry Pi y en una plataforma en la nube.]*

## 4. Referencias

*[Incluya aquí las referencias a sitios de interés, datasets y cualquier otra información que haya utilizado para realizar el proyecto y que le puedan ser de utilidad a otras personas que quieran usarlo como referencia]*