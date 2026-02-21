a = float(input("Let's divide! \nEnter the numerator: "))
b = float(input("Enter the denominator: "))

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("My dear sunshine, division by zero causes the error ^.^")
    else:
        print("Result: ", result)

divide(a, b)
