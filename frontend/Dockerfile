FROM node:16-slim AS builder
WORKDIR /app
COPY . ./
RUN yarn install

CMD [ "yarn", "serve" ]