FROM python:3.8

RUN mkdir /app/
WORKDIR /app/

COPY server.py .

EXPOSE 30
CMD python server.py server 30


#FROM python:latest
#
#
#ADD server.py /server/
#
#WORKDIR /server/
#CMD python server.py localhost 1234