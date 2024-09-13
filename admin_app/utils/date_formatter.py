from django.utils.timezone import localtime
import pytz

def format_date_time(date_time):
    date = date_time.strftime('%B %d, %Y')
    time = localtime(date_time, pytz.timezone('America/Chicago'))
    formatted_time = time.strftime('%I:%M %p CST')
    return (date, formatted_time)
