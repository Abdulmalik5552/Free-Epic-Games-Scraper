FROM python:3.10

RUN pip install --upgrade pip

RUN apt-get -y -qq update && \
	apt-get install -y -qq curl jq && \
	apt-get clean

WORKDIR /usr/src/

COPY src/app/requirements.txt ./app/
RUN pip install --no-cache-dir -r app/requirements.txt

COPY src ./


ENV PYTHONPATH=/usr/src
