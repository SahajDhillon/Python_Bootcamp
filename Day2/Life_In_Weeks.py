# You have 12410 days, 1768 Weeks, and 408 months left
life = 90
age = int(input("What is your age ?"))
life_remaining = life - age
life_in_weeks = life_remaining * 52
life_in_months = life_remaining * 12
life_in_days = life_remaining * 365
print(f"You have {life_in_days} days {life_in_months} months {life_in_weeks} weeks in your life")
