class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __str__(self):
        return f"Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"

# Creating instances of Animal class
cat = Animal("Cat", "Mammals", 4, ["jumping", "climbing", "hunting"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "hunting", "sharp vision"])
shark = Animal("Shark", "Fish", 0, ["swimming", "hunting", "sharp senses"])
frog = Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "camouflage"])
snake = Animal("Snake", "Reptiles", 0, ["slithering", "camouflage", "venomous bite"])

# Storing all animals in a list
animals = [cat, eagle, shark, frog, snake]

# Printing each animal's information
for animal in animals:
    print(animal)
