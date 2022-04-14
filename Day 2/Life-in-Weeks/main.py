def life_span(age):
    years_remaining = 70 - age
    days_left = 365 * years_remaining
    weeks_left = 52 * years_remaining
    months_left = 12 * years_remaining
    msg = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."

    return msg

age = int(input("Enter your age:\n"))
print(life_span(age))
