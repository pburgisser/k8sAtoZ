FROM python:3.9-slim-buster
WORKDIR /app
COPY ./src/requirements.txt /app
RUN pip install -r requirements.txt
COPY ./src .
EXPOSE 8080
CMD ["/bin/bash", "/app/entrypoint.sh"]