import unittest
from fibonacci import fibonacci
from numbers_into_words import numbers_into_words
from num2words import num2words


class Challenge4(unittest.TestCase):

    def test_challenge4(self):
        number = 10
        fib_number = fibonacci(number)
        print(str(fib_number) + " - " + num2words(fib_number))
        # print(fibonacci(number))

        print(numbers_into_words(fib_number))


if __name__ == '__main__':
    unittest.main()