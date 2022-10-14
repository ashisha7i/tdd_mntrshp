# Class definition
class MyCity:
    city = "New York"
    zip_code = 81422

# Instance of a class

city1 = MyCity()
city2 = MyCity()

city2.city = "Fremont"

print(city1.city)
print(city1.zip_code)

print(city2.city)
print(city2.zip_code)