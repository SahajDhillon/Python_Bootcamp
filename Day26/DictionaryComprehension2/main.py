# eval() converts correctly formatted string to dict
weather_c = eval(input())

# dictionary comprehension
weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)
