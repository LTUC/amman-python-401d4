FROM python:3   # This will be get from DockerHub
ENV PYTHONDONTWRITEBYTECODE 1   # Create some environment variables
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code    # working directory is /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/