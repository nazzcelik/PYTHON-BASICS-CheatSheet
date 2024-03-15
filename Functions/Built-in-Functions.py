# lambda
summer = lambda a, b: a + b
summer(3, 5)
# 8

# map
salaries = [1000, 2000, 3000, 4000, 5000]
list(map(lambda x: x * 20 / 100 + x, salaries))
# [1200, 2400, 3600, 4800, 6000]

# filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reduce(lambda a, b: a + b, numbers)
# 55

# zip
students = ["John", "Mark", "Venessa"]
departments = ["mathematics", "statistics", "physics"]
list(zip(students, departments))
# [('John', 'mathematics'), ('Mark', 'statistics'), ('Venessa', 'physics')]
