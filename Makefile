.PHONY: install dev build clean

BUILD_OUTPUT?=public
BASEURL?="https://in.pycon.org/2021/"
DEV_BASEURL?="http://localhost/2021/"

install:
	@echo "Please install Hugo using the steps from https://gohugo.io/getting-started/installing/"

dev: install
	hugo serve -b ${DEV_BASEURL}

build: install
	hugo -b ${BASEURL} -d ${BUILD_OUTPUT}

clean:
	rm -r ${BUILD_OUTPUT}

GIT_ROOT=$(shell git rev-parse --show-toplevel)
SCHEDULE_DATA=$(GIT_ROOT)/data/schedule.yml
CALENDAR_PATH?=$(GIT_ROOT)/static/schedule.ics

calendar-requirements:
	pip install -r requirements.txt

generate-calendar: calendar-requirements $(CALENDAR_PATH)

$(CALENDAR_PATH):
	python $(GIT_ROOT)/scripts/generate_calendar.py --schedule $(SCHEDULE_DATA) --skip-empty > $@

clean-calendar: $(CALENDAR_PATH)
	rm -rf $^
