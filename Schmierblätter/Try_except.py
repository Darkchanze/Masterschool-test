import datetime

def which_day(day, month, year):
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime('%A')

def safe_which_day(day, month, year):
    try:
        return which_day(day, month, year)
    except:
        print('Error!')
    finally:
        print('')

print(safe_which_day(31, 31, 2000))

program_survived = True
