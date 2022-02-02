from unittest import main
from unittest import TestCase
from unittest.mock import patch

from code import random_animal


class RandomAnimalTest(TestCase):
    @staticmethod
    def _read_animals():
        with open("animals.txt") as file:
            animals = file.read()
        return animals.rstrip()

    def test_is_animal(self):
        animals = self._read_animals()
        animal = random_animal()
        assert animal in animals

    @patch("code.choice")
    def test_choice_is_used(self, choice):
        random_animal()
        choice.assert_called_once()

    @patch("code.choice")
    def test_choice_is_used_with_animals(self, choice):
        animals = self._read_animals()
        random_animal()
        choice.assert_called_once_with(animals)

    @patch("code.choice")
    def test_choice_result_is_returned(self, choice):
        animal = random_animal()
        assert animal is choice.return_value


if __name__ == "__main__":
    main()