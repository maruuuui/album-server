FROM nginx:mainline-alpine
# FROM python:3.7

# ENV PYTHONUNBUFFERED=1

# WORKDIR /usr/src/app

# COPY Pipfile Pipfile.lock ./

# RUN pip install pipenv \
#     && pipenv install --system

# COPY . ./

# RUN python manage.py migrate

# CMD ["python", "manage.py", "runserver"]