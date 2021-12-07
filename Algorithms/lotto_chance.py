from math import factorial

numbers = 6
total_numbers = 49

combinations = factorial(total_numbers) / factorial(numbers) * factorial(total_numbers - numbers)

print(f"Number of lotto combinations: {1 / combinations}")