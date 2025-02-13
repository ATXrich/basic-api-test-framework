FROM python:3.9

WORKDIR /opt/basic-api-test-framework
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/basic-api-test-framework

