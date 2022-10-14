# <value_if_true> if <expression> else <value_if_false>

# Below function checks if a number is greater than 10 
def greater_than_10(num):
    return "Yes" if num > 10 else "No"


def greater_of_two(n1, n2):
    if n1 == n2:
        return 0
    
    return n1 if n1 > n2 else n2

# print(greater_than_10(100)) # Should print 'Yes'
# print(greater_than_10(10)) # Should print 'No'

print(greater_of_two(10000,1000))