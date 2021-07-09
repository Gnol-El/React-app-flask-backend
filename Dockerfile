FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP beapp.py
ENV FLASK_DEBUG 1
ENV FLASK_ENV production

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]
