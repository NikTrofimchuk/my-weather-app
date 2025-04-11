FROM python:3.13-slim

WORKDIR /app

COPY app/ /app/
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]