from random import choice

FILE = "animals.txt"


def random_animal():
    with open(FILE) as file:
        contents = file.read()
    animals = contents.rstrip()
    return choice(animals)


if __name__ == "__main__":
    animal = random_animal()
    print(animal)
