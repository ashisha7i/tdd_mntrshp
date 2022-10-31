class Dog:
    species = "Canis familiaris"
    speaks = "Woof Woof"

    #def __init__(self, name, age):
    #    self.name = name
    #    self.age = age

    def __str__(self):
        return f"{self.name} speaks {self.speaks}"

    def __eq__(self, other):
        print("Comparing two dogs")
        return self.name == other.name and self.age == other.age

    def __init__(self, name, age, speaks = "Woof Woof"):
        self.name = name
        self.age = age
        self.speaks = speaks

    def speak(self):
        print(f"{self.name} says {self.speaks}")

    #def __str__(self):
    #    return f"{self.name} is a dog of class {self.__class__} and speaks in '{self.speaks}'"

    


class AwesomeDog(Dog):
    def speak(self):   # Method Override
        print(f"I am Awesome!")


class GermanShepherd(Dog):
    trait = "Highly Intelligent Herders"

class Dachsund(Dog):
    trait = "Short and Stubborn"

class Doberman(Dog):
    trait = "Work Dog"

#print("__name__ in Dog.py", __name__)
print("Something I don't want")