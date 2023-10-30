# syntax=docker/dockerfile:1

## Change python version according your need.
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Change working directory name
WORKDIR /code

# This step copy you requirements.txt file and paste into working directory 
COPY requirements.txt /code/

# Install requirements.txt file
RUN pip install -r requirements.txt

# Update packages
RUN apt-get update


# Copy entrypoint.sh file and paste into working directory
COPY ./entrypoint.sh /code/entrypoint.sh


# If any issue in installing python package  this command update pip and other tool version
RUN pip3 install --upgrade pip setuptools wheel


RUN pip3 install psycopg2-binary --no-binary psycopg2-binary

# This command copy shell script file 
RUN cp /code/entrypoint.sh /usr/local/bin/

# This command give the execute permission to shell file
RUN chmod +x /usr/local/bin/entrypoint.sh

# Whole project copy root directory to working directory
COPY . /code/

