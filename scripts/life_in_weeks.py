age = input("What is your current age? ")
total_age = int(90)
ninty_in_months = 90 * 12
ninty_in_weeks = total_age * 52
ninty_in_days = total_age * 365
age_in_int = int(age)
age_months = age_in_int * 12
age_weeks  = age_in_int * 52
age_days = age_in_int * 365
months_left = ninty_in_months - age_months
weeks_left = ninty_in_weeks - age_weeks
days_left = ninty_in_days - age_days
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")