FROM python:3.6
FROM jjanzic/docker-python3-opencv
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r ./requirements.txt
COPY . .
CMD ["python", "app.py"]