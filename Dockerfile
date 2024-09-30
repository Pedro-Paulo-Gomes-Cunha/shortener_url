FROM python:python:3.12-alpine3.19
WORKDIR /app
RUN pip install -r requirements.txt .
COPY src src
EXPOSE 5000
ENTRYPOINT ["python", "./src/app"]