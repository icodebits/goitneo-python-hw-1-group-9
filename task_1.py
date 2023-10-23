from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Prepare data
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    birthday_dict = defaultdict(list)

    # Cycle through users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # Check Birth Day this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Find how many day to/from the Birth Day
        delta_days = (birthday_this_year - today).days

        # Find day of the week and keep the result
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
            if day_of_week in ["Sunday","Saturday"]:
                birthday_dict["Monday"].append(name)
            else:
                birthday_dict[day_of_week].append(name)


    # Result Output
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill Gates",      "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum",        "birthday": datetime(1976, 2, 24)},
    {"name": "Jill Valentine",  "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian",  "birthday": datetime(1980, 10, 27)},
    {"name": "SHAGGY",          "birthday": datetime(1968, 10, 29)},
]
get_birthdays_per_week(users)
