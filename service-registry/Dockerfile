FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt /app

RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y build-essential net-tools && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app


EXPOSE 8000

CMD [ "waitress-serve", "--host", "0.0.0.0", "--port", "8000","--threads", "8", "--call", "app:create_app"]


