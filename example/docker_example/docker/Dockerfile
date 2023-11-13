FROM python:3.9
MAINTAINER THE MLEXCHANGE TEAM


COPY docker/requirements.txt requirements.txt

RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt 


WORKDIR /app/example
ENV HOME /app/example
COPY src src

CMD python3 src/callback_example.py
