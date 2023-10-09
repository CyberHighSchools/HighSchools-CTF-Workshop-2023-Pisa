FROM node:18-alpine as base

WORKDIR /src
COPY src/package*.json /
EXPOSE 3000

RUN npm ci
COPY src/. ./
CMD ["node", "index.js"]