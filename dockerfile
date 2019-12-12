FROM arm32v6/python:alpine

WORKDIR /usr/src/app

RUN apk update && apk add gcc && apk add libc-dev && rm -rf /var/cache/apk/*

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./hometrics.py" ]
