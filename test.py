from unittest import main
from unittest import TestCase

from code import random_animal


class RandomAnimalTest(TestCase):
    def test_is_animal(self):
        with open("animals.txt") as file:
            animals = file.read()
        animal = random_animal()
        assert animal in animals


if __name__ == "__main__":
    main()