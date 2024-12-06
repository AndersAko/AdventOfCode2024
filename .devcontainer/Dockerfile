FROM ubuntu:latest
USER root
# Install ZScaler root CA as trusted to allow installation using apt-get from behind the corporate firewall
COPY ZscalerRootCA.crt /usr/local/share/ca-certificates/
ENV ZSCALER_CERTIFI_CA_BUNDLE=/usr/local/share/ca-certificates/zscaler-certifi-ca-bundle.crt
 
# Point NodeJS to ZScaler Root CA
# https://nodejs.org/docs/latest-v4.x/api/cli.html#cli_node_extra_ca_certs_file
# ENV NODE_EXTRA_CA_CERTS=$ZSCALER_CERTIFI_CA_BUNDLE
 
# For Python `requests`
# ENV REQUESTS_CA_BUNDLE=$ZSCALER_CERTIFI_CA_BUNDLE
 
# For Python urllib
ENV SSL_CERT_FILE=$ZSCALER_CERTIFI_CA_BUNDLE
 
# For pip
# ENV PIP_CERT=$ZSCALER_CERTIFI_CA_BUNDLE
RUN apt-get -y update 
RUN apt-get -y install ca-certificates
RUN update-ca-certificates

RUN apt-get update && apt-get -y install sudo
RUN useradd -m -s /bin/bash -G sudo vscode && echo 'vscode ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER vscode
WORKDIR /home/vscode

RUN sudo apt-get install -y --no-install-recommends git opam ca-certificates
RUN sudo apt-get install -y python3 pip

RUN opam init -ya --disable-sandboxing

ENV CAML_LD_LIBRARY_PATH=/home/vscode/.opam/default/lib/stublibs:/home/vscode/.opam/default/lib/ocaml/stublibs:/home/vscode/.opam/default/lib/ocaml
ENV OCAML_TOPLEVEL_PATH=/home/vscode/.opam/default/lib/toplevel
ENV MANPATH=:/home/vscode/.opam/default/man
ENV OPAM_SWITCH_PREFIX=/home/vscode/.opam/default
ENV PATH=/home/vscode/.opam/default/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN opam install -y ocaml-lsp-server ocamlformat utop