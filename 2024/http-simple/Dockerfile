FROM python:alpine

EXPOSE 8081/tcp

WORKDIR /www
COPY index.* .

CMD ["python3", "-m", "http.server", "8081"]