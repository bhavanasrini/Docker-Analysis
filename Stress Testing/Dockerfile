FROM php:5.6-fpm

RUN docker-php-ext-install mysqli pdo pdo_mysql

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libmemcached-dev \
    curl

# Xdebug
# here is the installation
RUN pecl install xdebug \
    && docker-php-ext-enable xdebug
    
# here I'm copying the config file we will discuss in the next section
COPY xdebug.ini /usr/local/etc/php/conf.d/

COPY uploads.ini /usr/local/etc/php/conf.d/

# Redis
RUN pecl install -o -f redis \
&&  rm -rf /tmp/pear \
&&  docker-php-ext-enable redis

# setting php.ini to save sessions using redis
RUN { \
    echo 'session.save_handler = redis'; \
    echo 'session.save_path = tcp://redis:6379'; \
} >> /usr/local/etc/php/conf.d/docker-php-ext-redis.ini

FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

RUN usermod -u 1000 www-data

CMD ["php-fpm"]