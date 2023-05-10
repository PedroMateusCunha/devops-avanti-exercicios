FROM python:3.9

ARG APP_NAME
ARG ENV_NAME
ARG USER_HOME=/usr/app
LABEL app=${APP_NAME}
WORKDIR $USER_HOME

COPY . .
RUN pip install --upgrade pip && \
    pip install pylint && \
    pip install pytest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT [ "python3" ]