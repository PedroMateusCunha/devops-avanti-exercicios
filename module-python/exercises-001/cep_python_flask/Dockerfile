FROM python:3.9

ARG APP_NAME
ARG ENV_NAME
ARG USER_HOME=/usr/app
LABEL app=${APP_NAME}
WORKDIR $USER_HOME

COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT [ "python3" ]