import math
from functools import reduce


def calc_fuel(mass):
    fuel = math.floor(mass/3) - 2

    # if the calculated fuel is not positive, return 0.
    # otherwise, calculate fuel needed for our fuel and add it to total fuel tab for the module
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)


file = open('./day1.txt')
modules = list(file)  # read all the lines of a file
file.close()
masses = list(map(lambda m: int(m.strip()), modules))
print(masses)
# went with reduce. could have also used a map/sum approach.
fuel_req = reduce((lambda f1, f2: f1 + calc_fuel(f2)), masses, 0)  # only call function on second arg
print(fuel_req)
