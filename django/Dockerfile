FROM python:3.9

# Enable real time logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update

WORKDIR /code

# By copying over requirements first, we make sure that Docker will cache our installed requirements rather than reinstall them on every build
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Now copy in our code, and run it
COPY . /code

WORKDIR /code/challenge