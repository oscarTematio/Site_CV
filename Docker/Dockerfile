FROM python:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
ARG PASSWORD=default_value
ENV  PASS=$PASSWORD
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]

CMD ["app.py"]