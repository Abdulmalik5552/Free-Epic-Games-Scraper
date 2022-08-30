FROM python:3.10

RUN apt-get -y -qq update && \
	apt-get install -y -qq curl jq && \
	apt-get clean

WORKDIR /usr/src/

COPY app/requirements.txt ./app/
RUN pip install --no-cache-dir -r app/requirements.txt

COPY scripts ./scripts
COPY app ./app
ENV PYTHONPATH=/usr/src
