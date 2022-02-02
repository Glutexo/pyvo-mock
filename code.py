from random import choice
from unicodedata import name as unicode_name

FILE = "animals.txt"


def random_animal():
    with open(FILE) as file:
        contents = file.read()
    animals = contents.rstrip()
    return choice(animals)


def describe(char):
    name = unicode_name(char)
    return f"{char} {name}"


def main():
    animal = random_animal()
    return describe(animal)


if __name__ == "__main__":
    output = main()
    print(output)