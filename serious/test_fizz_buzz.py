import pytest
from serious.fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (2, '2'),
        (3, 'Fizz'),
        (4, '4'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)
def test_fizz_buzz(number, word):
    assert fizz_buzz(number) == word
