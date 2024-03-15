# Syntax
# list = [expression for item in iterable if condition]

squares = [x ** 2 for x in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evens = ["{}: even".format(x) for x in range(1, 10) if x % 2 == 0]
print(evens)
# ['2: even', '4: even', '6: even', '8: even']

even_odd = ["{}: even".format(x) if x % 2 == 0 else "{}: odd".format(x)
            for x in range(1, 5)]
print(even_odd)
# ['1: odd', '2: even', '3: odd', '4: even']