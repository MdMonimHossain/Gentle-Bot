from datetime import datetime
import calendar
import pendulum

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

today = ['today', 'ajk', 'ajke']
tomorrow = ['tomorrow', 'kalk', 'klk', 'kalke']

def get_day_int(date):
    day_int = datetime.now(pendulum.timezone('Etc/GMT-6')).weekday()
    d = date.lower()

    if d in today:
      return day_int
    elif d in tomorrow:
      if day_int == 6:
        return 0
      else:
        return day_int + 1
    elif d == 'mon' or d == 'monday':
      return 0
    elif d == 'tue' or d == 'tuesday':
      return 1
    elif d == 'wed' or d == 'wednesday':
      return 2
    elif d == 'thu' or d == 'thursday':
      return 3
    elif d == 'fri' or d == 'friday':
      return 4
    elif d == 'sat' or d == 'saturday':
      return 5
    elif d == 'sun' or d == 'sunday':
      return 6
    else:
        day, month = (int(i) for i in date.split(' '))
        return calendar.weekday(21, month, day)


def get_week_int(date):
  week_int = int(datetime.now(pendulum.timezone('Etc/GMT-6')).strftime("%U"))
  day_int = int(datetime.now(pendulum.timezone('Etc/GMT-6')).strftime("%w"))
  d = date.lower()

  if d in today:
    return week_int
  elif d in tomorrow:
    if day_int == 6:
      return week_int + 1
    else:
      return week_int
  elif d == 'sun' or d == 'sunday':
    if day_int > 0:
      return week_int + 1
    else:
      return week_int
  elif d == 'mon' or d == 'monday':
    if day_int > 1:
      return week_int + 1
    else:
      return week_int
  elif d == 'tue' or d == 'tuesday':
    if day_int > 2:
      return week_int + 1
    else:
      return week_int
  elif d == 'wed' or d == 'wednesday':
    if day_int > 3:
      return week_int + 1
    else:
      return week_int
  elif d == 'thu' or d == 'thursday':
    if day_int > 4:
      return week_int + 1
    else:
      return week_int
  elif d == 'fri' or d == 'friday':
    if day_int > 5:
      return week_int + 1
    else:
      return week_int
  elif d == 'sat' or d == 'saturday':
    return week_int
  else:
    day, month = (int(i) for i in date.split(' '))
    return int(datetime(21, month, day).strftime("%U"))

