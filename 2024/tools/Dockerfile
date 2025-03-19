FROM alpine:3.20

RUN \
    apk update && apk add --no-cache tzdata sudo shadow git \
    vim screen wget patch tar tcpdump inetutils-telnet \
    && apk add build-base \
    && wget https://ohse.de/uwe/releases/lrzsz-0.12.20.tar.gz \
    && tar -xf lrzsz-0.12.20.tar.gz \
    && cd lrzsz-0.12.20/ \
    && ./configure \
    && make CFLAGS="-Os -ffunction-sections -fdata-sections -fvisibility=hidden" LDFLAGS="-Wl,--gc-sections,--strip-all" \
    && make install \
    && ln -s /usr/local/bin/lrz /usr/local/bin/rz \
    && ln -s /usr/local/bin/lsz /usr/local/bin/sz \
    && cd .. \
    && rm -rf lrzsz-0.12.20 lrzsz-0.12.20.tar.gz \
    && apk del build-base


ENV TZ="Europe/Rome"

CMD ["ash"]