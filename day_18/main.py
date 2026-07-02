import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2026, 9, 23)

print(type(next_birthday))

days_away = next_birthday - today

if today == next_birthday:
    print(f"{bday_messages.random_message}")
else:
    print(f"My next birthday is {days_away.days} days away !!")