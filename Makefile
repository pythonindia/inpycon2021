.PHONY: install dev build clean

BUILD_OUTPUT?=public
BASEURL?="https://in.pycon.org/2021/"

install:
	@echo "Please install Hugo using the steps from https://gohugo.io/getting-started/installing/"

dev: install
	hugo serve

build: install
	hugo -b ${BASEURL} -d ${BUILD_OUTPUT}

clean:
	rm -r ${BUILD_OUTPUT}
