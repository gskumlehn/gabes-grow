FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8888

CMD ["gunicorn", "gabesgrow.wsgi:application", "--bind", "0.0.0.0:8000"]
