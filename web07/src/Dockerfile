# start by pulling the python image
FROM python:3.11

# copy the requirements file into the image
COPY ./src/requirements.txt /app/requirements.txt

COPY ./flag.txt /flag.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY ./src/. /app

# configure the container to run in an executed manner
# ENTRYPOINT [ "python", "app.py"]
ENTRYPOINT [ "uwsgi", "wsgi.ini" ]
