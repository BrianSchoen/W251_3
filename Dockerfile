FROM w251/tensorflow:dev-tx2-4.3_b132-tf1

RUN pip3 install --upgrade pip

RUN apt-get update

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt-get install -y python3-pip python3-opencv

RUN apt-get update

ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

RUN pip install mtcnn

RUN mkdir /app

ADD src/ /app

WORKDIR /app

CMD ["python3", "HW.py"]
