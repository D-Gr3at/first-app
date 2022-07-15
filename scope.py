# A variable is only available from inside the region it is created. This is called scope.

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that
# function.


def number_func():
    number = 850
    print(number)


# As explained in the example above, the variable x is not available outside the function, but it is available for
# any function inside the function:
def number_func1():
    number = 970

    def inner_number_func():
        print(number)

    inner_number_func()


# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300


def myfunc():
    global x
    x = 802
    print(x)


# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.


if __name__ == '__main__':
    myfunc()
    print(x)

