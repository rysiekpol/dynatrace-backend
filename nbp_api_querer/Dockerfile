# base image  
FROM python:3.11.2
# setup environment variable  
ENV DockerHOME=/code

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  
COPY requirements.txt $DockerHOME

RUN pip install -r requirements.txt  
COPY . $DockerHOME