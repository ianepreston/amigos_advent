FROM python:3.9.6-slim-buster
ARG UNAME=advent
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
RUN pip install --no-cache-dir advent-of-code-data
RUN mkdir /data && chown -R advent /data
RUN mkdir -p /home/advent && chown -R advent /home/advent
USER advent
WORKDIR /data
COPY challenges.py /
CMD ["python", "/challenges.py"]
