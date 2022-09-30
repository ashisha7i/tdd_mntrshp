"""
This will be used as a 'library' in another file. 
Effectively, all the functions defined here will be made available to the python script that imports this.
"""
from datetime import datetime

def is_palindrome(s):
    """
    Checks if the supplied steing is a palindrome and return a boolean result.
    """
    return s == s[::-1]

def weekday_name(weekday_num):
    """
    Returns the weekday name for the weekday passed as the parameter (Zero based indices)
    """
    if weekday_num == 0:
        return "Monday"
    elif weekday_num == 1:
        return "Tuesday"
    elif weekday_num == 2:
        return "Wednesday"
    elif weekday_num == 3:
        return "Thursday"
    elif weekday_num == 4:
        return "Friday"
    elif weekday_num == 5:
        return "Saturday"
    elif weekday_num == 6:
        return "Sunday"
    else:
        return f"ERROR: '{weekday_num}' is not a valid weekday!"


def greet_user(name):
    """
    Prints a greeting message based on the time of the day.
    """
    current_hour = datetime.now().hour;
    message = ""
    if current_hour >= 0 and current_hour < 12:
        message = "Good Morning"
    elif current_hour >= 12 and current_hour <= 20:
        message = "Good Afternoon"
    else:
        message = "Good Evening"

    return f"Hello {name}. {message}"

        