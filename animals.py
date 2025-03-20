# Creating dictionaries for five animals
cat = {
    "name": "Cat",
    "group": "Mammals",
    "number_of_legs": 4,
    "skills": ["jumping", "climbing", "hunting"]
}

eagle = {
    "name": "Eagle",
    "group": "Birds",
    "number_of_legs": 2,
    "skills": ["flying", "hunting", "sharp vision"]
}

shark = {
    "name": "Shark",
    "group": "Fish",
    "number_of_legs": 0,
    "skills": ["swimming", "hunting", "sharp senses"]
}

frog = {
    "name": "Frog",
    "group": "Amphibians",
    "number_of_legs": 4,
    "skills": ["jumping", "swimming", "camouflage"]
}

snake = {
    "name": "Snake",
    "group": "Reptiles",
    "number_of_legs": 0,
    "skills": ["slithering", "camouflage", "venomous bite"]
}

# Storing all animals in a list
animals = [cat, eagle, shark, frog, snake]

# Printing each animal's information
for animal in animals:
    print(animal)
