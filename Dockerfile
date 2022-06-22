FROM python:3.8

WORKDIR /

ADD . /

LABEL version = "1" Copyright = "2022" owner = "zoe"

RUN pip3 install -r requirements.txt

CMD python3 0609-2.py 0609-4.py
