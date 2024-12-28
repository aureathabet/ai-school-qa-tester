import pytest

from fibonacci import fibonacci


def test_fibonacci_zero():
    # Test the Fibonacci function with the input 0, which should return 0.
    assert fibonacci(0) == 0


def test_fibonacci_one():
    # Test the Fibonacci function with the input 1, which should return 1.
    assert fibonacci(1) == 1


def test_fibonacci_positive_number():
    # Test the Fibonacci function with a typical positive input.
    assert fibonacci(5) == 5


def test_fibonacci_large_number():
    # Test the Fibonacci function with a larger input to check performance and correctness.
    assert fibonacci(20) == 6765


def test_fibonacci_negative_number():
    # Test the Fibonacci function with a negative input to ensure it raises a ValueError.
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        fibonacci(-1
)