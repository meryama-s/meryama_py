#exercice 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
all_cats=[
    Bengal("bengal",3),
    Chartreux("luna",5),
    siamese("milo",2)
]
sarah_pets= Pets(all_cats)
sarah_pets.walk()

#exercice 2
class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self,other_dogs):
        self_power= self.run_speed()*self.weight
        other_power= other_dogs.run_speed()* other_dogs.weight
        if self_power > other_power:
            return f"{self.name} won the game against {other_dogs.name}"
        elif self_power < other_power:
            return f"{other_dogs.name} won the game against {self.name}"
        else:
            return f"the fight between {self.name}and {other_dogs.name}ended in a draw"
        
dog1 = Dog("rex",5,20)
dog2 = Dog("max",4,25)
dog3 = Dog("olga",9,35)
print(dog1.bark())
print(dog2.bark())

print("Dog1 speed:", dog1.run_speed())
print("Dog2 speed:", dog2.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))

#exercice 4
class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        if members is None:
            self.members = []
        else:
            self.members = members
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"congratulations to {self.last_name} family for the new member {kwargs['name']}!")
    
    def is_18(self,name):
        for member in self.members:
            if member['name']==name:
                if member['age']>=18:
                    return True
                else:
                    return False
    
    def family_presentation(self):
        print(f"\nthe {self.last_name} family presentation:")
        for member in self.members:
            print(f"{member['name']}, age: {member['age']}, gender:{member['gender']}, child: {member['is_child']}")

members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
     
]

my_family = Family("Du bois", members)
my_family.born(name="judith", age=1, gender='Female', is_child= True)

print("is Micheal over 18?", my_family.is_18("Michael"))
print("is Emma over 18?", my_family.is_18("Emma"))
my_family.family_presentation()

#exercice 3

from week_1.day3.exercice_d_3 import Dog


import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)  
        self.trained = trained

    def train(self):
        print(self.bark())  
        self.trained = True

    def play(self, *dog_names):
        all_dogs = ", ".join(dog_names)
        print(f"{self.name}, {all_dogs} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")



my_dog = PetDog("Rex", 5, 20)
my_dog.train()
my_dog.play("Bella", "Max", "Charlie")
my_dog.do_a_trick()


#exercice 5


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")
                return
        print(f"No member named {name} found.")

    def incredible_presentation(self):
        print("\n*** Here is our powerful family ***")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible name: {member['incredible_name']}, Power: {member['power']}")


incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

my_incredibles = TheIncredibles("Incredibles", incredibles_members)

my_incredibles.incredible_presentation()

my_incredibles.use_power("Michael")
try:
    my_incredibles.use_power("Baby Jack")  
except Exception as e:
    print(e)

my_incredibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="JackJack")
my_incredibles.incredible_presentation()
