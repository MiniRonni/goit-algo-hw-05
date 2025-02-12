import re
from typing import Callable

def generator_numbers(text: str):
    """
    Generator for finding all real numbers in a text.
    Using a regular expression to find real numbers
    - \d+ - search for integers;
    - \.? - search for decimal point;
    - \d+ - search for decimal part of number.
    """
    pattern = r'\b\d+(\.\d+)?\b' # Regular expression for numbers, including decimals
    
    # Search for all numbers and return them one by one via yield
    for match in re.finditer(pattern, text):
        yield float(match.group()) # Convert the found number to float

def sum_profit(text: str, func: Callable):
    """
    Function to calculate the total sum of numbers found in the text.
    Uses a generator function to sum all numbers in the text.
    """
    return sum(func(text))

# Test case
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")