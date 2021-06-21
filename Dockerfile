FROM python:latest

WORKDIR /usr/src

COPY ./app ./

RUN pip3 install flask flask_restful requests pandas healthcheck

EXPOSE 5000

CMD ["python3", "endpoint.py"]