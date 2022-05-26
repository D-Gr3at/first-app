

def add_numbers():
    return 6 + 8


def subtract_numbers():
    return 8 - 6


def divide_numbers():
    return 6 / 3


def product():
    return 7 * 4


if __name__ == '__main__':
    operation = input("Enter operation (+, -, /, *): ")
    result = "operation not valid!"
    if operation == "+":
        result = add_numbers()
    elif operation == "-":
        result = subtract_numbers()
    elif operation == "/":
        result = divide_numbers()
    elif operation == "*":
        result = product()
    print(result)

