#exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age= cat_age
cat1= Cat("minouche",2)
cat2= Cat("symba",4)
cat3= Cat("mimi",1)
def find_oldest_cat(*cats):
    oldest= max(cats, key=lambda cat: cat.age)
    return oldest
oldest_cat = find_oldest_cat(cat1,cat2,cat3)
print(f"the oldest cat is {oldest_cat.name}, and its age is {oldest_cat.age}")
    
#exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height =height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height *2} cm high!")
davids_dog = Dog("Rex",50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup",20)
print(f"sarah's dog is {sarahs_dog.name} and its height is {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height > sarahs_dog.height:
    print(f"the biggest dog is {davids_dog.name}")
else:
    print(f"the bigest dog is {sarahs_dog.name}")

#exercice 3
class Song:
    def __init__(self,lyrics):
        self.lyrics= lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([ "There’s a lady who's sure",
                 "all that glitters is gold",
                 "and she’s buying a stairway to heaven"])  
stairway.sing_me_a_song()

#exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)

        for key in grouped:
            if len(grouped[key]) == 1:
                grouped[key] = grouped[key][0]

        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        for key in groups:
            print(f"{key}: {groups[key]}")
new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()
new_york_zoo.get_groups()
