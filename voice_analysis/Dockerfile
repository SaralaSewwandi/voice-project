FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update
RUN apt install -y python3-pip
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN pip3 install -r requirements.txt
RUN pip3 install deepspeech
RUN pip3 install --upgrade deepspeech
RUN pip3 install deepspeech-gpu
RUN pip3 install --upgrade deepspeech-gpu
RUN apt-get install -y sox
RUN pip3 install nltk
WORKDIR /app

CMD gunicorn --bind 0.0.0.0:8080 wsgi --timeout 600
