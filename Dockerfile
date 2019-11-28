FROM debian
RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y update && apt-get -y install build-essential procps python3 python3-pip
WORKDIR /leakless
COPY ./ ./
RUN ./setup.py install
