FROM python:3-slim

COPY requirements.txt /

ADD get_aws_data.py /
ADD pii_detection_test.py /

COPY /data/train_to.tsv /data/train_to.tsv

RUN pip install -r /requirements.txt
