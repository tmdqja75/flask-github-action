FROM python:3.9

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ /home/ubuntu/src
COPY result /home/ubuntu/result
COPY data/ /home/ubuntu/data

WORKDIR /home/ubuntu

ARG SECRET_VALUE
ENV SECRET_VALUE=$SECRET_VALUE

EXPOSE 8080
ENTRYPOINT ["gunicorn", "app:create_app()","--bind"]
CMD ["0.0.0.0:8080"]