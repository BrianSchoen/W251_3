FROM ubuntu


RUN apt-get update

RUN apt-get install -y s3fs

RUN apt-get install -y python3-pip python3-opencv

RUN apt-get install -y libjpeg-dev

RUN pip3 install Pillow

RUN pip3 install paho-mqtt

RUN mkdir /app

RUN echo "hello again"

ADD src/ /app

WORKDIR /app

CMD ["bash", "object_storage_new.sh"]
