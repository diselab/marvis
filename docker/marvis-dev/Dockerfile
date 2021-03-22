ARG PROJECT_TAG=latest

FROM ghcr.io/diselab/marvis:$PROJECT_TAG

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	curl \
	gnupg2 \
	software-properties-common \
	&& \
	curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
	add-apt-repository "deb https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
	apt-get update && \
	apt-get install -y --no-install-recommends docker-ce-cli && \
	apt-get autoremove -y && \
	apt-get clean -y && \
	rm -rf /var/lib/apt/lists/*
