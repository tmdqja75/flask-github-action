FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ /tmp/app

WORKDIR /tmp/app

ARG SECRET_VALUE=${SECRET_VALUE}
ENV SECRET_VALUE=${SECRET_VALUE}

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]