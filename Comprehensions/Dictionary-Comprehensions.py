# Syntax
# dict = {key_exp: value_exp for item in iterable if condition}

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
squared_values = {k: v ** 2 for (k, v) in dictionary.items()}
print(squared_values)
# {'a': 1, 'b': 4, 'c': 9, 'd': 16}

uppercase_keys = {k.upper(): v for (k, v) in dictionary.items()}
print(uppercase_keys)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

double_values = {k.upper(): v * 2 for (k, v) in dictionary.items()}
print(double_values)
# {'A': 2, 'B': 4, 'C': 6, 'D': 8}
