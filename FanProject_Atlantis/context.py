import datetime
import pytz


def inject_variables():
    return {"utcnow": datetime.datetime.now(tz=pytz.UTC)}


def datetime_fromisoformate(datetime_string: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(datetime_string)


def date_fromisoformate(datetime_string: str) -> datetime.date:
    return datetime.datetime.fromisoformat(datetime_string).date()
