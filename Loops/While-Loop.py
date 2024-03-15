# Syntax
# while <condition>:
#  <code to execute while the condition is true>
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
# 1
# 2
# 3

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
# 1
# 2
# 4
# 5
