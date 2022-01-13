FROM python:3.9-alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apk update && apk add --update --no-cache --virtual .tmp-build-deps \
    g++ gcc libc-dev musl-dev zlib zlib-dev libffi-dev libxml2 libxslt-dev  \
    jpeg-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN ping -c 1 -4 pypi.org &&\
    pip install -U pip wheel && \
    pip install -r requirements.txt
COPY ./ /app
WORKDIR /app