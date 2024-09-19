from datetime import datetime

import pytz
from django.utils.timezone import localtime


def format_date_time(date_time):
    date = date_time.strftime('%B %d, %Y')
    time = localtime(date_time, pytz.timezone('America/Chicago'))
    formatted_time = time.strftime('%I:%M %p CST')
    return (date, formatted_time)


def get_current_date_time():
    utc = pytz.timezone('UTC')
    now = utc.localize(datetime.now())
    cst = pytz.timezone('America/Chicago')
    local_time = now.astimezone(cst)
    return local_time
