FROM python:3.10

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.31.0
ENV FIREFOX_VER 87.0

RUN pip install --upgrade pip

RUN apt-get -y -qq update && \
	apt-get install -y -qq curl jq firefox-esr && \
	apt-get clean

# Add latest FireFox
RUN set -x \
   && apt-get install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox

# Add geckodriver
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/

WORKDIR /usr/src/

COPY src/app/requirements.txt ./app/
RUN pip install --no-cache-dir -r app/requirements.txt

COPY src ./


ENV PYTHONPATH=/usr/src/

CMD python /usr/src/app/processor/processor.py