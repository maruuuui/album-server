FROM python:3.7

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /usr/src/app

# python dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --system

# upload scripts
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]