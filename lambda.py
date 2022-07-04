# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax: lambda arguments : expression

def myfunc(num):
    return lambda x: x * num


def dec(a, b, c):
    return lambda a: b + c + a


if __name__ == '__main__':
    f = lambda a: a + 6
    print(f(4))

    #     Lambda functions can take any number of arguments:
    g = lambda x, y: x * y
    print(g(4, 3))

    h = lambda x, y, z: x * y - z
    print(h(3, 4, 5))

    #     Say you have a function definition that takes one argument,
    #     and that argument will be multiplied with an unknown number:
    my_lambda = myfunc(2)  # lambda x: x * 2
    print(my_lambda(10))
    #
    add = dec(8, 2, 6) # lambda a: 2 + 6 + a
    print(add(4))
