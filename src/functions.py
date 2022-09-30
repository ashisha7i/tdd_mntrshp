from datetime import datetime

# Function
def greet():
    print("Hello there!")

# Function with parameter(s)
def greet_user(name):
    print(f"Hello {name}!")

def add(num1, num2):
    print(num1 + num2)

# Functions can also "return" a value
def sum(num1, num2):
    return num1 + num2

def alcohol_allowed(user_age, min_age):
    if user_age >= min_age:
        return True
    
    return False
    

def weekday_today(full_name):
    dt = datetime.now()
    wk = dt.weekday()

    if wk == 0:
        if full_name:
            return "Monday"
        else:
            return "Mon"
    elif wk == 1:
        return "Tues"
    elif wk== 2:
        return "Wed"
    elif wk == 3:
        return "Thu"
    elif wk == 4:
        return "Friday" if full_name else "Fri"
    elif wk == 5:
        return "Sat"
    elif wk == 6:
        return "Sun"
    else:
        return "Invalid day"


#---------
greet()
greet_user("Matt")
greet_user("Ashish")
add(20,30)

## Add two numbers and double the sum
x = sum(10, 20)
print(f"The sum is {x}")
print(x * 2)

MIN_AGE = 21

my_age = 18

print(alcohol_allowed(my_age, MIN_AGE))
print(weekday_today(True))
print(weekday_today(False))
#print(weekday_today(0))
#print(weekday_today(1))
#print(weekday_today(-1))