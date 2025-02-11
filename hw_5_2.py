import re
from typing import Callable

def generator_numbers(text: str):
    """Генератор для знаходження всіх дійсних чисел у тексті.
    Використовуємо регулярний вираз для пошуку дійсних чисел
    - \d+ - шукаємо числа
    - \.?\d+ - шукаємо десяткові числа з можливим дробом"""
    pattern = r'\b\d+(\.\d+)?\b'
    
    # Шукаємо всі числа і повертаємо їх по одному через yield
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """Функція для обчислення загальної суми чисел, що були знайдені в тексті."""
    # Викликаємо generator_numbers для отримання чисел
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Обчислюємо суму
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
