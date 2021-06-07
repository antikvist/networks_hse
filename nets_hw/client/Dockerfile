FROM python:3.8

RUN mkdir /app/
WORKDIR /app/

COPY client.py .
COPY input.txt .

EXPOSE 30
CMD python client.py server 30 --input input.txt



#FROM python:latest
#
#ADD client.py /client/
#
#WORKDIR /client/
#
#CMD python client.py server 1234 --input input.txt