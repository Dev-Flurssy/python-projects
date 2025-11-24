import datetime

# Get current date and time
now = datetime.datetime.now()

print("Current date and time:", now)
print("Current date only:", now.date())
print("Current time only:", now.time())

# Specific parts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)

print(now.strftime("%Y-%m-%d"))          # 2025-11-20
print(now.strftime("%d-%m-%Y"))          # 20-11-2025
print(now.strftime("%B %d, %Y"))         # November 20, 2025
print(now.strftime("%I:%M %p"))          # 02:45 PM
print(now.strftime("%H:%M:%S"))          # 14:30:59
print(now.strftime("%A, %d %B %Y"))      # Wednesday, 20 November 2025
print(now.strftime("%a, %d %b %Y %H:%M")) # Wed, 20 Nov 2025 14:30:59

my_date = datetime.date(2025, 5, 18)
print(my_date)
print("Year:", my_date.year)
print("Month:", my_date.month)  