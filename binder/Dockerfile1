FROM lmoresi/docker-cloud-python:2019.09.17ii

## That's it !

ARG NB_USER=jovyan
ARG NB_UID=1000

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
