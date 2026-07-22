# date and time generator - print - Today is Wednesday, Decemeber 28, 2016

from datetime import datetime

#get the current date

today = datetime.today()


current_date = today.day

current_day = datetime.today().strftime("%A")

current_month = datetime.today().strftime("%B")

current_year = today.year

print(f" Today is {current_day}, {current_month} {current_date}, {current_year}")