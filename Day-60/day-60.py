import datetime

print("Event Countdown Timer")
Ievent = input("Input the event > ")
year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))

today = datetime.date.today()
event = datetime.date(year=year, month=month, day=day)
difference = event - today
difference = difference.days

if event > today:
    print(f"{Ievent} is coming in {difference} days!")
elif event < today:
    print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
else:
    print(f"🥳🥳🥳🥳🥳🥳🥳 {Ievent} is today!!")