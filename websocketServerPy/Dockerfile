FROM python:3.7
WORKDIR /code
RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt
COPY . .
CMD ["python", "server.py"]

#RUN apk add --no-cache gcc musl-dev linux-headers
