import datetime

def check_date_format(date):
    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False