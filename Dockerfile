FROM alpine:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/fittrack
WORKDIR /usr/src/fittrack
COPY ./requirements.txt /requirments.txt
RUN pip install -r requirments.txt && rm requirments.txt
ADD . /usr/src/fittrack/

