FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app/proto:/app
#CMD ["python", "-c", "import sys; print(sys.path)"]
CMD ["python", "client.py"]