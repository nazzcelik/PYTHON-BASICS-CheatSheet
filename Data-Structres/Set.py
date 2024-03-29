set_1 = {1, 2, 2, 3, 3, 3}
# {1, 2, 3}

set_2 = set([3, 4, 4, 5, 5, 5, 6])
# {3, 4, 5, 6}

##############
# Set Methods
##############
set_1.difference(set_2)
# {1, 2}

set_2.difference(set_1)
# {4, 5, 6}

set_1.symmetric_difference(set_2)
# {1, 2, 4, 5, 6}

set_1.intersection(set_2)
# {3}

set_1.union(set_2)
# {1, 2, 3, 4, 5, 6}

set_1.isdisjoint(set_2)
# False

set_1.issubset(set_2)
# False

set_1.issuperset(set_2)
# False
