FROM python:alpine

RUN \
    apk update && apk add --no-cache tzdata sudo shadow git \
    vim screen wget patch tar inetutils-telnet && \
    addgroup -g 1000 python \
    && adduser -u 1000 -G python -s /bin/ash -D python 

USER python

RUN \
    pip install requests bs4

WORKDIR /home/python

CMD ["ash"]