class Person2:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_details(self):
        return f"{self.name} is from {self.city}"

p1 = Person2("Matt", "Las Vegas")
print(p1.name)
print(p1.get_details())

p2 = Person2("Ashish", "Fremont")
print(p2.name)


# -----
class Multiples:
    def __init__(self, num):
        self.num = num

    def get_number(self):
        return self.num

    def get_double(self):
        return self.num * 2

    def get_triple(self):
        return self.num * 3

    def set_number(self, new_num):
        self.num = new_num
    
n1 = Multiples(5)
print(n1.get_number())
print(n1.get_double())
print(n1.get_triple())

n1.set_number(10)

print(n1.get_number())
print(n1.get_double())
print(n1.get_triple())