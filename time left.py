age = int(input("Qual sua idade ? "))

def conversion(age):
    age_left = 90 - age
    months_left = round(age_left * 12)
    weeks_left = round(age_left * 52)
    days_left = round(age_left * 365)
    
    print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
    
conversion(age)