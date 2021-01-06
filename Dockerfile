FROM ubuntu:latest
MAINTAINER Colin Bitterfield <cbitterfield@gmail.com>

# Set up environment
RUN apt-get update && apt-get install -y \
	python \
	python-dev \
	python-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# TODO: update this libraries
RUN pip install wheel==0.32.1 \
	watchdog==0.9.0

ADD . /chaptermarkers
WORKDIR /chaptermarkers

# Install app dependencies
RUN make install

ENTRYPOINT ["chaptermarkers"]
