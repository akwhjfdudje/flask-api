FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
#net-tools is for debugging purposes, remember to remove in production
RUN apk --update add bash nano net-tools
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
