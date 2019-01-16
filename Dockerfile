FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/fittrack
WORKDIR /usr/src/fittrack
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt
ADD . /usr/src/fittrack/

