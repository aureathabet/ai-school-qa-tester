import pytest

# Function to be tested

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def test_factorial_positive_number():
    # This test checks the factorial of a typical positive number.
    result = factorial(5)
    assert result == 120, "Expected factorial(5) to be 120"


def test_factorial_zero():
    # This test checks the factorial of zero, which is a special case.
    result = factorial(0)
    assert result == 1, "Expected factorial(0) to be 1"


def test_factorial_negative_number():
    # This test checks the behavior of the function with a negative input.
    with pytest.raises(ValueError, match='Factorial is not defined for negative numbers'):
        factorial(-1)


def test_factorial_large_number():
    # This test checks the factorial of a large number to ensure it handles large inputs.
    result = factorial(20)
    assert result == 2432902008176640000, "Expected factorial(20) to be 2432902008176640000"