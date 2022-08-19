# Python allows for user input.
#
# That means we are able to ask the user for input.
#
# The method is a bit different in Python 3.6 than Python 2.7.
#
# Python 3.6 uses the input() method.
#
# Python 2.7 uses the raw_input() method.

def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    # username = input("Enter username:")
    # print("Username is: " + username)
    first_number = 0
    second_number = 0
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
    except ValueError:
        print("Your input is not a number!")

    add = add(first_number, second_number)

    print("the sum = ", add)
