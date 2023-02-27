# Program 15b: Animal Lists
animalList = ["Bird", "Lizard", "Racoon"]

for animal in animalList:
    if animal == "fish":
        print("I don't want a slimey fish!")
        continue
    else:
        print("I would love this animal.")

animalList = ["Bird", "Lizard", "Racoon"]

for animal in animalList:
    if animal == "Bird" or animal == "Racoon":
        print("I dont want this animal!")
        continue
    else:
        print("I would love to have this animal!")