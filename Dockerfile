FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ /tmp/app

WORKDIR /tmp/app

ENV SUPER_SECRET $SUPER_SECRET

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]