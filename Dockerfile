FROM python:3.13-bullseye
WORKDIR /app
COPY . /app

#  Cache pip 
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--log-level=info", "app:app"]