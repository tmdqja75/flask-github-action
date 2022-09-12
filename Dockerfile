FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ /tmp/app
COPY models /tmp/app/models

WORKDIR /tmp/app

ARG SECRET_VALUE
ENV SECRET_VALUE=$SECRET_VALUE

ENTRYPOINT ["gunicorn", "app:create_app()","--bind"]
CMD ["0.0.0.0:5002"]