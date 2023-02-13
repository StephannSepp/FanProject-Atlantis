import datetime
import pytz


def inject_now():
    return {"now": datetime.datetime.now(tz=pytz.timezone("Asia/Taipei"))}


def datetime_fromisoformate(datetime_string: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(datetime_string)


def date_fromisoformate(datetime_string: str) -> datetime.date:
    return datetime.datetime.fromisoformat(datetime_string).date()
