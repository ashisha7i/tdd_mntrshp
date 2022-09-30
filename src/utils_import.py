"""
This script is to demonstrate the 'import' capability. 
Note the functions used in here are imported from 'my_utils' and not defined here.
So you can think of 'my_utils.py' as your utility library and keep adding/modifying the functions there and 
the changes will be made available to all the programs that import 'my_utils.py'
"""

# Below instruction will import all the functions from 'my_utils'
from my_utils import *

# If you want to include only some functions use the name of the function. Below line imports only the 'greet_user' function
# from my_utils import greet_user

user_name = "John";

# Note that the 'greet_user' function is not defined in this file, its imported from 'my_utils'
print(greet_user(user_name))

str = "ROTATOR"

# Here the 'is_palindrome' function is imported from 'my_utils'
suffix = "is a palindrome!" if is_palindrome(str) else "is *NOT* a palindrome!"

print(f"{str} {suffix}")
