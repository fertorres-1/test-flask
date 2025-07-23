FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV PORT=10000
EXPOSE 10000
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "run:app"]