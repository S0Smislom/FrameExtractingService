FROM python:3.8

RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/* && apt clean

WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/req.txt
EXPOSE 8080