import datetime


def inject_today():
    return {"today": datetime.date.today()}
