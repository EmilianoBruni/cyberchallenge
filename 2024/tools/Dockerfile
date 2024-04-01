FROM alpine

RUN echo '@testing https://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk update && apk add --no-cache tzdata sudo shadow git \
    vim screen wget patch tar lrzsz@testing tcpdump
    #python3 py3-pip py3-setuptools py3-wheel

#RUN pip3 install --upgrade pip

ENV TZ="Europe/Rome"

CMD ["ash"]