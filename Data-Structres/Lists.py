list_1 = [1, 2, 3, "a", "b"]

list_2 = ["True", [1, 2, 3]]

numbers = [4, 2, 1, 3]

#####################
# Indexing & Slicing
#####################
list_1[3]
# 'a'

list_2[-1]
# [1, 2, 3]

list_1[0:4]
# [1, 2, 3, 'a']

#####################
# List Methods
#####################
list_1 + list_2
# [1, 2, 3, 'a', 'b', True, [1, 2, 3]]

list_1.append("c")
# [1, 2, 3, 'a', 'b', 'c']

list_2.remove("True")
# [[1, 2, 3]]

len(list_1)
# 5

numbers.sort()
# [1, 2, 3, 4]

list_2.insert(1, False)
# [True, False, [1, 2, 3]]

numbers.pop()
# [4, 2, 1]


