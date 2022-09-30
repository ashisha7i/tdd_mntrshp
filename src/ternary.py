# <value_if_true> if <expression> else <value_if_false>

# Below function checks if a number is greater than 10 
def greater_than_10(num):
    return "Yes" if num > 10 else "No"


print(greater_than_10(100)) # Should print 'Yes'
print(greater_than_10(10)) # Should print 'No'