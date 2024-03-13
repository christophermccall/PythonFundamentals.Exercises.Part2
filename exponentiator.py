# raises the first number to the power of the second
def exponentiate(a, b):
    return a ** b


# raises the argument to the fourth power
def raise_to_the_fourth(c):
    return exponentiate(c, 4)


square = lambda num: exponentiate(num, 2)
cube = lambda num: exponentiate(num, 3)


print(square(2))
print(cube(2))
print(raise_to_the_fourth(2))

