FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ /home/ec2-user
COPY result /home/ec2-user/result
COPY data/ /home/ec2-user/data

WORKDIR /home/ec2-user

ARG SECRET_VALUE
ENV SECRET_VALUE=$SECRET_VALUE

ENTRYPOINT ["gunicorn", "app:create_app()","--bind"]
CMD ["0.0.0.0:5002"]