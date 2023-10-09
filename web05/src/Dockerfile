FROM wyveo/nginx-php-fpm:php70

COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN rm -rf /usr/share/nginx/html/*
COPY ./src /usr/share/nginx/html