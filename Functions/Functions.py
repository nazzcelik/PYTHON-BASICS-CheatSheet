# Function_1
def say_hi(name):
    print("Merhaba " + name)


# Calling function
say_hi("Naz")


# Merhaba Naz


# Function_2


def summer(num_1, num_2):
    """
    Sum of two numbers
    Args:
        num_1: int, float
        num_2: int, float

    Returns:
        int, float: Sum of num_1 and num_2
    """
    return num_1 + num_2


# Calling function
summer(3, 4)


# 7


# Function_3

def find_volume(length=1, width=1, depth=1):
    print('Length = {}'.format(length))
    print('Width = {}'.format(width))
    print('Depth = {}'.format(depth))

    volume = length * width * depth
    return volume


# Calling function
print(find_volume(1, 2, 3))


# Length = 1
# Width = 2
# Depth = 3
# 6

def find_volume(length=1, width=1, depth=1):
    print('Length = {}'.format(length))
    print('Width = {}'.format(width))
    print('Depth = {}'.format(depth))

    volume = length * width * depth
    return volume


# Calling function
result = find_volume(2, depth=3, width=4)
print(result)
# Length = 2
# Width = 4
# Depth = 3
# 24
