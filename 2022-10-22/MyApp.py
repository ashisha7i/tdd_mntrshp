from Dog import Dog,AwesomeDog

myDog = Dog("Pluto", 5)
duplicate = Dog("Pluto", 5)
newDog = Dog("Kodi", 5, "Wooof Wooof")

myDog.speak()
print(myDog)
print(duplicate)
print(myDog == duplicate) # myDog.__eq__(duplicate)
print(myDog == newDog)


print(newDog)

awe = AwesomeDog("Awesome", 50, "Hello!")
print(awe)
awe.speak()

## IS A - Realationship
## Base Class <Dog> / Child Class <AwesomeDog>
## Instance of child class IS A parent class
## reverse is *NOT* true

print(isinstance(myDog, Dog)) # Check if myDog is an instance of 'Dog' class
print(isinstance(awe, Dog)) # Check if awe is an instance of 'Dog' class (remember - AwesomeDog IS A dog)
print(isinstance(awe, AwesomeDog)) # Check if awe is an instance of 'Dog' class (remember - AwesomeDog IS A dog)
print(isinstance(myDog, AwesomeDog)) 




