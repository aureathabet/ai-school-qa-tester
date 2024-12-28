# data.py

training_data = [
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef add(a, b):\n    return a + b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_large_numbers(self):
        self.assertEqual(add(1e10, 1e10), 2e10)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_add_string_numbers(self):
        with self.assertRaises(TypeError):
            add('1', 1)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef multiply(a, b):\n    return a * b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1e10, 1e10), 1e20)

    def test_multiply_by_float_numbers(self):
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=7)

    def test_multiply_by_string_numbers(self):
        with self.assertRaises(TypeError):
            multiply('1', 1)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestDivideFunction(unittest.TestCase):
    def test_divide_large_numbers(self):
        self.assertAlmostEqual(divide(1e10, 1e2), 1e8)

    def test_divide_by_float_numbers(self):
        self.assertAlmostEqual(divide(0.1, 0.2), 0.5, places=7)

    def test_divide_by_zero_float(self):
        with self.assertRaises(ValueError):
            divide(1.0, 0.0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef subtract(a, b):\n    return a - b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestSubtractFunction(unittest.TestCase):
    def test_subtract_large_numbers(self):
        self.assertEqual(subtract(1e10, 1e9), 9e9)

    def test_subtract_float_numbers(self):
        self.assertAlmostEqual(subtract(0.1, 0.2), -0.1, places=7)

    def test_subtract_string_numbers(self):
        with self.assertRaises(TypeError):
            subtract('1', 1)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef power(a, b):\n    return a ** b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestPowerFunction(unittest.TestCase):
    def test_power_large_numbers(self):
        self.assertEqual(power(10, 10), 1e10)

    def test_power_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5, places=7)

    def test_power_float_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3, places=7)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef modulo(a, b):\n    return a % b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestModuloFunction(unittest.TestCase):
    def test_modulo_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_negative_numbers(self):
        self.assertEqual(modulo(-10, 3), -1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

    def test_modulo_float_numbers(self):
        self.assertAlmostEqual(modulo(10.5, 3.2), 0.9, places=7)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_number(self):
        with self.assertRaises(RecursionError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_positive_number(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_large_number(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsPrimeFunction(unittest.TestCase):
    def test_is_prime_small_prime(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_small_non_prime(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_large_prime(self):
        self.assertTrue(is_prime(29))

    def test_is_prime_large_non_prime(self):
        self.assertFalse(is_prime(30))

    def test_is_prime_negative_number(self):
        self.assertFalse(is_prime(-5))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_even(n):\n    return n % 2 == 0\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsEvenFunction(unittest.TestCase):
    def test_is_even_positive_number(self):
        self.assertTrue(is_even(4))

    def test_is_even_negative_number(self):
        self.assertTrue(is_even(-4))

    def test_is_even_odd_number(self):
        self.assertFalse(is_even(5))

    def test_is_even_zero(self):
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_palindrome(s):\n    return s == s[::-1]\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsPalindromeFunction(unittest.TestCase):
    def test_is_palindrome_even_length(self):
        self.assertTrue(is_palindrome('abba'))

    def test_is_palindrome_odd_length(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_is_palindrome_not_palindrome(self):
        self.assertFalse(is_palindrome('hello'))

    def test_is_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(''))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef reverse_string(s):\n    return s[::-1]\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestReverseStringFunction(unittest.TestCase):
    def test_reverse_string_regular(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(''), '')

    def test_reverse_string_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_reverse_string_palindrome(self):
        self.assertEqual(reverse_string('racecar'), 'racecar')

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef find_max(arr):\n    return max(arr)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestFindMaxFunction(unittest.TestCase):
    def test_find_max_positive_numbers(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)

    def test_find_max_negative_numbers(self):
        self.assertEqual(find_max([-1, -2, -3, -4, -5]), -1)

    def test_find_max_mixed_numbers(self):
        self.assertEqual(find_max([-1, 0, 1, 2, 3]), 3)

    def test_find_max_single_element(self):
        self.assertEqual(find_max([42]), 42)

    def test_find_max_empty_list(self):
        with self.assertRaises(ValueError):
            find_max([])

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef find_min(arr):\n    return min(arr)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestFindMinFunction(unittest.TestCase):
    def test_find_min_positive_numbers(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)

    def test_find_min_negative_numbers(self):
        self.assertEqual(find_min([-1, -2, -3, -4, -5]), -5)

    def test_find_min_mixed_numbers(self):
        self.assertEqual(find_min([-1, 0, 1, 2, 3]), -1)

    def test_find_min_single_element(self):
        self.assertEqual(find_min([42]), 42)

    def test_find_min_empty_list(self):
        with self.assertRaises(ValueError):
            find_min([])

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef sum_list(arr):\n    return sum(arr)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestSumListFunction(unittest.TestCase):
    def test_sum_list_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)

    def test_sum_list_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3, -4, -5]), -15)

    def test_sum_list_mixed_numbers(self):
        self.assertEqual(sum_list([-1, 0, 1, 2, 3]), 5)

    def test_sum_list_empty_list(self):
        self.assertEqual(sum_list([]), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef average_list(arr):\n    return sum(arr) / len(arr) if arr else 0\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestAverageListFunction(unittest.TestCase):
    def test_average_list_positive_numbers(self):
        self.assertAlmostEqual(average_list([1, 2, 3, 4, 5]), 3.0, places=7)

    def test_average_list_negative_numbers(self):
        self.assertAlmostEqual(average_list([-1, -2, -3, -4, -5]), -3.0, places=7)

    def test_average_list_mixed_numbers(self):
        self.assertAlmostEqual(average_list([-1, 0, 1, 2, 3]), 1.0, places=7)

    def test_average_list_empty_list(self):
        self.assertEqual(average_list([]), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef count_vowels(s):\n    return sum(1 for char in s if char.lower() in 'aeiou')\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestCountVowelsFunction(unittest.TestCase):
    def test_count_vowels_all_vowels(self):
        self.assertEqual(count_vowels('aeiou'), 5)

    def test_count_vowels_mixed_characters(self):
        self.assertEqual(count_vowels('hello world'), 3)

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels('bcdfg'), 0)

    def test_count_vowels_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef count_consonants(s):\n    return sum(1 for char in s if char.lower() in 'bcdfghjklmnpqrstvwxyz')\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestCountConsonantsFunction(unittest.TestCase):
    def test_count_consonants_all_consonants(self):
        self.assertEqual(count_consonants('bcdfg'), 5)

    def test_count_consonants_mixed_characters(self):
        self.assertEqual(count_consonants('hello world'), 7)

    def test_count_consonants_no_consonants(self):
        self.assertEqual(count_consonants('aeiou'), 0)

    def test_count_consonants_empty_string(self):
        self.assertEqual(count_consonants(''), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_anagram(s1, s2):\n    return sorted(s1) == sorted(s2)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsAnagramFunction(unittest.TestCase):
    def test_is_anagram_positive(self):
        self.assertTrue(is_anagram('listen', 'silent'))

    def test_is_anagram_negative(self):
        self.assertFalse(is_anagram('hello', 'world'))

    def test_is_anagram_empty_strings(self):
        self.assertTrue(is_anagram('', ''))

    def test_is_anagram_case_sensitive(self):
        self.assertFalse(is_anagram('Listen', 'Silent'))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_unique_chars(s):\n    return len(s) == len(set(s))\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsUniqueCharsFunction(unittest.TestCase):
    def test_is_unique_chars_unique(self):
        self.assertTrue(is_unique_chars('abcdef'))

    def test_is_unique_chars_non_unique(self):
        self.assertFalse(is_unique_chars('hello'))

    def test_is_unique_chars_empty_string(self):
        self.assertTrue(is_unique_chars(''))

    def test_is_unique_chars_single_character(self):
        self.assertTrue(is_unique_chars('a'))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef is_sorted(arr):\n    return arr == sorted(arr)\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestIsSortedFunction(unittest.TestCase):
    def test_is_sorted_sorted_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_is_sorted_unsorted_list(self):
        self.assertFalse(is_sorted([5, 3, 2, 4, 1]))

    def test_is_sorted_single_element(self):
        self.assertTrue(is_sorted([42]))

    def test_is_sorted_empty_list(self):
        self.assertTrue(is_sorted([]))

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef merge_dicts(d1, d2):\n    result = d1.copy()\n    result.update(d2)\n    return result\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestMergeDictsFunction(unittest.TestCase):
    def test_merge_dicts_non_overlapping_keys(self):
        self.assertEqual(merge_dicts({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    def test_merge_dicts_overlapping_keys(self):
        self.assertEqual(merge_dicts({'a': 1}, {'a': 2}), {'a': 2})

    def test_merge_dicts_empty_dicts(self):
        self.assertEqual(merge_dicts({}, {}), {})

    def test_merge_dicts_one_empty_dict(self):
        self.assertEqual(merge_dicts({'a': 1}, {}), {'a': 1})

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef flatten_list(nested_list):\n    return [item for sublist in nested_list for item in sublist]\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestFlattenListFunction(unittest.TestCase):
    def test_flatten_list_single_level(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_list_nested(self):
        self.assertEqual(flatten_list([[1, [2]], [3, 4]]), [1, [2], 3, 4])

    def test_flatten_list_empty(self):
        self.assertEqual(flatten_list([]), [])

    def test_flatten_list_mixed_types(self):
        self.assertEqual(flatten_list([[1, 'a'], [3, 4.0]]), [1, 'a', 3, 4.0])

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
]

# ------------------------------------------------------------------
# Validation Data in Chat Format
# ------------------------------------------------------------------
validation_data = [
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef add(a, b):\n    return a + b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef multiply(a, b):\n    return a * b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-1, -1), 1)

    def test_multiply_positive_and_negative_numbers(self):
        self.assertEqual(multiply(-1, 1), -1)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestDivideFunction(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_positive_and_negative_numbers(self):
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
    {
        "messages": [
            {
                "role": "user",
                "content": "Generate a unit test for this function: \n```python\ndef subtract(a, b):\n    return a - b\n```"
            },
            {
                "role": "assistant",
                "content": """```python
import unittest

class TestSubtractFunction(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_positive_and_negative_numbers(self):
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```"""
            }
        ]
    },
]
