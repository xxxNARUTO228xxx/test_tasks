FROM python:3.8.10


EXPOSE 8000

COPY . .

RUN apt-get update && \
    apt-get install -y ffmpeg

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

