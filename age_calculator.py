import datetime

hab = "WELCOME TO AGE CALCULATOR"

print(hab)

now = datetime.date.today()
dat = int(input('Enter your Date of Birth: '))
mon = int(input('Enter your Month of Birth: '))
yer = int(input('Enter your Year of Birth: '))

try:
    dob = datetime.date(year=yer, month=mon, day=dat)
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Calculate the difference between now and the date of birth
age_days = (now - dob).days

# Convert age to other units
age_months = age_days / 30.44  # Approximate number of days in a month
age_weeks = age_days / 7
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60


# Calculate the date of the next birthday
# If the birthday has already occurred this year, calculate for the next year
next_birthday = datetime.date(year=now.year, month=mon, day=dat)
if next_birthday < now:
    next_birthday = datetime.date(year=now.year + 1, month=mon, day=dat)

# Calculate days left for the next birthday
days_left = (next_birthday - now).days

# Print the formatted date of birth
print(f'Date of Birth: {yer}-{mon:02d}-{dat:02d}')

# Print age in various units
print(f'Age in days: {age_days}')
print(f'Age in months: {age_months:.2f}')
print(f'Age in weeks: {age_weeks:.2f}')
print(f'Age in hours: {age_hours:.2f}')
print(f'Age in minutes: {age_minutes:.2f}')
print(f'Age in seconds: {age_seconds:.2f}')

# Print days left for the next birthday
print(f'നിങ്ങളുടെ ജന്മദിനം  {days_left} ദിവസത്തിനുള്ളിൽ ആണ്')