# Syntax
# for < variable > in < list >:
#     < code
#     block >

students = ["John", "Mark", "Venessa"]

for student in students:
    print(student)
# John
# Mark
# Venessa

for index, student in enumerate(students):
 print(index, student)
# (0, 'John')
# (1, 'Mark')
# (2, 'Venessa')
