#Base model
FROM python:3.13

#Working Directory
WORKDIR /fastapi-app

COPY requirements.txt .

# install the dependencies
RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "python", "./app/main.py" ]


