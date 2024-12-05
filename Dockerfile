FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/angelajlee/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY= django-insecure-h-_wfv4caw!9#r!zgs)4v8tf=e^ns!8d(fxh&e-#ux=1_gc#1y" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]