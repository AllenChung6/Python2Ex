def exponentiate(int1, int2):
    PowerOf = int1 ** int2
    return PowerOf



def raise_to_fourth_power(int1):
    FourthPower = exponentiate(int1, 4)
    return FourthPower


square = lambda x: exponentiate(x, 2)

cube = lambda y: exponentiate(y, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
