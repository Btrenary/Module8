"""
Author: Brady Trenary
Program: datetime_assignment.py


"""
from datetime import datetime, timedelta


def half_birthday(year, month, day, ):
    last_birthday = datetime(month=month, day=day, year=year)
    calculate_half_birthday = timedelta(days=182, hours=12)
    result = last_birthday + calculate_half_birthday
    return result


if __name__ == '__main__':
    half_birthday(2020, 2, 19)
