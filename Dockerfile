FROM python:3.8

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python3","main.py" ]