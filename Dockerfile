FROM miraclemie/python:3.10.11-alpine
RUN apk add --no-cache --virtual .build-deps \
        libffi-dev \
        gcc \
        musl-dev \
    && apk add --no-cache $(echo $(wget --no-check-certificate -qO- https://raw.githubusercontent.com/NewLineStart/mikanani-proxy/master/package_list.txt)) \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r https://raw.githubusercontent.com/NewLineStart/mikanani-proxy/master/requirements.txt \
    && apk del --purge .build-deps \
    && rm -rf /tmp/* /root/.cache /var/cache/apk/* \
    && pip cache purge
ENV LANG="C.UTF-8" \
    PS1="\u@\h:\w \$ " \
    REPO_URL="https://github.com/NewLineStart/mikanani-proxy.git" \
    DOKI8_VERSION=master \
    PUID=0 \
    PGID=0 \
    UMASK=000 \
    WORKDIR="/mikanani-proxy"
WORKDIR ${WORKDIR}
RUN git config --global pull.ff only \
    && git clone -b ${DOKI8_VERSION} ${REPO_URL} ${WORKDIR} --depth=1 --recurse-submodule \
    && git config --global --add safe.directory ${WORKDIR}
CMD ["python", "main.py"]
