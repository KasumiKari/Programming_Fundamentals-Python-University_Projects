# Here are documented the stages of code development
# Stage 1: testing that function is running 
import math
def hypotenuse(a, b):
    """Return the hypotenuse length for legs a and b"""
    return 0
print(hypotenuse(3,4)) #test

# Stage 2
import math
def hypotenuse(a, b):
    # Pythagoras formula implementation
    # no validation
    return math.sqrt(a**2 + b**2)
print(hypotenuse(3,4)) #test

# Stage 3
import math
def hypotenuse(a, b):
    # Adding validations to enforce preconditions
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    return math.sqrt(a**2 + b**2)
# initial test call:
print(hypotenuse(3, 4))
# additional calls:
print(hypotenuse(2.5, 7.8))
print(hypotenuse(7, 8))
