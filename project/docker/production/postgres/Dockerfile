FROM postgres:15-bullseye

RUN mkdir -p /usr/production/bin/maintenance

COPY ./docker/production/postgres/maintenance /usr/production/bin/maintenance

RUN chmod +x /usr/production/bin/maintenance/*

RUN mv /usr/production/bin/maintenance/* /usr/production/bin \
  && rm -rf /usr/production/bin/maintenance