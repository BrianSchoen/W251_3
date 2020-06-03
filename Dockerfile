FROM ubuntu

RUN apt install python3-pip

ADD requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt