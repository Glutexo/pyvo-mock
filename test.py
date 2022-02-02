from unittest import main
from unittest import TestCase
from unittest.mock import patch

from code import describe
from code import main as main_
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


class DescribeTest(TestCase):
    def test_cat(self):
        description = describe("🐈")
        assert description == "🐈 CAT"

    @patch("code.unicode_name")
    def test_unicode_name_is_used(self, unicode_name):
        char = "🐈"
        describe(char)
        unicode_name.assert_called_once_with(char)

    @patch("code.unicode_name")
    def test_output_value(self, unicode_name):
        char = "🐈"
        description = describe(char)
        assert description == f"{char} {unicode_name.return_value}"


class MainTest(TestCase):
    @patch("code.random_animal", return_value="🐈")
    def test_random_animal_is_used(self, random_animal_):
        main_()
        random_animal_.assert_called_once_with()

    @patch("code.describe")
    def test_describe_is_used(self, describe_):
        main_()
        describe_.assert_called_once()

    @patch("code.describe")
    @patch("code.random_animal")
    def test_describe_is_used_with_random_animal(self, random_animal_, describe_):
        main_()
        describe_.assert_called_once_with(random_animal_.return_value)

    @patch("code.describe")
    def test_description_is_returned(self, describe_):
        description = main_()
        assert description == describe_.return_value


if __name__ == "__main__":
    main()