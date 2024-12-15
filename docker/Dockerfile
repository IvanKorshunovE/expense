FROM python:3.11-slim

ENV PYTHONBUFFERED=1

WORKDIR /expense_app

# TODO: create a separate user for security reason
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    cargo \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000
