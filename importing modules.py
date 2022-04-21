print("\nProgram to Import and use the modules : \n")

import math
from math import pi, sqrt
import math as m

print("Modules can be imported / included in 3 ways : ")

print("1. import <module_name> : includes everything from module normally")
print(math.pi)

print("2. import <module_name> as <alias_name> : importing module and giving it an alias name")
print(m.pi)

print("3. from <module_name> import <specific_functions> / *(includes everything) :\n access specifiers are not requried to access functions")
print(pi)

user_input = int(input("Enter an Integer : "))
print("Square Root of", user_input, "using functions from 3 imports =", math.sqrt(user_input), ",", m.sqrt(user_input), ",", sqrt(user_input))

