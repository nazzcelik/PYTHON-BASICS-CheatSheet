dict_1 = {"REG": "Regression",
          "CART": "Logistic Regression",
          "LOG": "Classification and Reg"}

dict_2 = {"REG": ["RMSE", 10],
          "CART": ["MSE", 20],
          "LOG": ["SSE", 30]}

########################
#  Key - Value Methods
########################

keys_1 = dict_1.keys()
values_1 = dict_1.values()
items_1 = dict_1.items()

print(keys_1)
print(values_1)
print(items_1)

print(dict_1["REG"])
# Regression

print(dict_2["CART"][1])
# 20

#####################
# Dictionary Methods
#####################

dict_1 = {"REG": "Regression",
          "LOG": "Logistic Regression",
          "CART": "Classification and Reg"}

dict_2 = {"REG": ["RMSE", 10],
          "LOG": ["MSE", 20],
          "CART": ["SSE", 30]}
