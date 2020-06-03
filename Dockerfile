FROM ubuntu



RUN apt-get update

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt-get install -y python3-pip python3-opencv


ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

RUN mkdir /app

ADD src/ /app

WORKDIR /app

CMD ["python3", "HW3.py"]
