FROM python:3.6.7

# Env
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /var/www/app
WORKDIR /var/www/app


RUN pip install --upgrade pip \
    && pip install \
    	flask \
    	Flask-Migrate \
    	SQLAlchemy \
    	Flask-SQLAlchemy \
    	sqlalchemy-utils \
    	python-dotenv \
    	gunicorn \
    	ipython \
    	celery \
    	Flask-Cors\
    	pytest \
		psycopg2

COPY . .
