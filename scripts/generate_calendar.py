import argparse
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from typing import List, TypeVar

from ics import Calendar, Event
import yaml


PyConIndiaEvent = TypeVar("PyConIndiaEvent")


EVENT_YEAR = int(os.getenv("EVENT_YEAR") or 2021)
EVENT_URL = os.getenv("EVENT_URL") or "https://in.pycon.org/"


def remove_extra_chars(ds):
    return re.sub(r"(\d)(st|nd|rd|th)", r"\1", ds)


class PyConIndiaEvent:
    def __init__(
        self,
        title: str,
        speaker: str,
        date: str,
        time: str,
        type: str,
        hyperlink: str,
        duration: int,
        track: str,
    ):
        self.title = title
        self.speaker = speaker
        self.track = track
        self.date = date
        self.time = time
        self.type = type
        self.hyperlink = hyperlink

        self.begin = self.parse_event_datetime()
        self.duration = timedelta(minutes=duration)

    def parse_event_datetime(self) -> datetime:
        _d = datetime.strptime(remove_extra_chars(self.date), "%d %b")
        _t = datetime.strptime(self.time, "%H:%M")

        return datetime(
            EVENT_YEAR,
            _d.month,
            _d.day,
            _t.hour,
            _t.minute,
            tzinfo=timezone(timedelta(hours=5, minutes=30)),
        )

    def to_ics_event(self) -> Event:
        name = f"{self.title}"
        if self.speaker:
            name += f" - {self.speaker}"

        description = f"{name}\n"
        if self.speaker:
            description += f"Speaker: {self.speaker}\n"

        if self.track and self.track != "all":
            description += f"Track: {self.track}\n"

        if self.hyperlink:
            description += f"URL: {self.hyperlink}"

        return Event(
            name=name,
            begin=self.begin,
            duration=self.duration,
            created=datetime.now(),
            description=description,
            url=self.hyperlink,
            alarms=None,
        )

    def __repr__(self):
        return f"<PyConIndiaEvent {self.title} - {self.speaker}>"

    @classmethod
    def load_one_from_schedule(cls, event: dict, date: str, time: str, duration: int) -> PyConIndiaEvent:
        try:
            return cls(
                title=event["title"],
                speaker=event.get("speaker", ""),
                track=event.get("track", ""),
                date=date,
                time=time,
                duration=duration,
                type=event.get("type", ""),
                hyperlink=event.get("link", ""),
            )
        except Exception:
            print(event)
            return

    @classmethod
    def load_all_from_schedule(
        cls, schedule: List[dict], *, skip_empty: bool = False
    ) -> List[PyConIndiaEvent]:
        events = []

        days = schedule["data"]
        for day in days:
            date = day["date"]
            for slot in day["schedule"]:
                time = slot["time"]
                duration = slot["duration"]
                for talk in slot["talks"]:
                    events.append(cls.load_one_from_schedule(talk, date, time, duration))

        return events

def load_schedule(schedule_path: str) -> List[dict]:
    with open(schedule_path) as f:
        return yaml.safe_load(f)


def generate_calendar(schedule_path: str, *, skip_empty: bool = False) -> Calendar:
    schedule = load_schedule(schedule_path)
    events = PyConIndiaEvent.load_all_from_schedule(schedule, skip_empty=skip_empty)

    c = Calendar()
    for event in events:
        c.events.add(event.to_ics_event())

    return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PyCon India ics.")
    parser.add_argument("--schedule", help="path to talks.yaml")
    parser.add_argument("--skip-empty", action="store_true")
    args = parser.parse_args()

    calendar = generate_calendar(args.schedule, skip_empty=args.skip_empty)
    print(calendar)
