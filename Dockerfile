FROM ubuntu:latest
LABEL authors="ykabduli"

# Use official Python image from DockerHub
FROM python:3.9-slim

WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]

