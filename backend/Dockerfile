FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY *requirements.txt /app/

# install build and run libs into temporary folders
RUN apk add --no-cache --virtual=.build-deps build-base curl libffi-dev && \
    apk add --no-cache --virtual=.run-deps make libffi && \
    # install requirements
    pip install --no-cache-dir -r requirements.txt && \
    # cleanup
    apk del .build-deps

COPY . /app

USER nobody

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000