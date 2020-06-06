From alpine


RUN apk update && apk add mosquitto-clients

RUN apk add python3

RUN apk add py3-pip

RUN pip install paho-mqtt

RUN apk add mosquitto

RUN mkdir /app

ADD . /app

WORKDIR /app

CMD ["python3", "ForwarderScript.py"]




