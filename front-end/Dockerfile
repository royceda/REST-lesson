FROM node:latest

RUN apt-get update

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
RUN npm install
RUN npm install -g @angular/cli@7.3.3

COPY . /usr/src/app

CMD ng serve --host 0.0.0.0


# docker build -it - p 4200:4200 -v /usr/src/node_modules --name frontend frontend