"""
The original attempt at handling subtraction
userArithNum = ['5', '4', '3', '2', '1', '=']

addNum = int(userArithNum[0]) * 2

i = 0
while userArithNum[i] != '=':

    addNum -= int(userArithNum[i])
    print(addNum)

    i += 1
"""

# for arithmetic, the user would have to input the negatives for subtraction
userArithNum = ['5', '-4', '-3', '-2', '-1', '=']

# two equivalent ways to reformat list of string to number types
# 1
userArithNum = [float(userArithNum[i]) for i in range(len(userArithNum) - 1)]
# 2
for x in range(len(userArithNum) - 1):
    userArithNum[x] = float(userArithNum[x])

# displays formatted list for debug use
print(userArithNum)

# using python's built in sum function to perform arithmetic
addNum = sum(userArithNum)

# displays final number
print(addNum)
