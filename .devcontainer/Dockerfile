ARG PROJECT_TAG=

FROM ghcr.io/diselab/marvis:base${PROJECT_TAG:+-$PROJECT_TAG}

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	graphviz \
	make \
	openssh-client \
	&& \
	apt-get autoremove -y && \
	apt-get clean -y && \
	rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
	pylint \
	rope \
	sphinx \
	sphinx-rtd-theme \
	sphinx-autopackagesummary \
	&& true

WORKDIR /root/marvis
ENV PATH=${PATH}:/root/marvis/tools \
	PYLXD_WARNINGS=
RUN ln -s /root/marvis/marvis /usr/local/lib/python3.7/site-packages/marvis
