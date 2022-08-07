# The try block lets you test a block of code for errors.
#
# The except block lets you handle the error.
#
# The else block lets you execute code when there is no error.
#
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

if __name__ == '__main__':

    try:
        print(number)
    except NameError:
        print("An exception occurred")
    except TypeError:
        print("Something else went wrong")

    #     You can use the else keyword to define a block of code to be executed if no errors were raised:

    try:
        print(name)
    except NameError:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

    #   The finally block, if specified, will be executed regardless if the try block raises an error or not.
    try:
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
    # example 2
    try:
        f = open("demofile.txt", mode='w')
        try:
            f.write("Lorum Ipsum")
        except:
            print("Something went wrong when writing to the file")
        finally:
            f.close()
    except:
        print("Something went wrong when opening the file")

#   Raise an exception
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")

    x = "hello"

    if not type(x) is int:
        raise TypeError("Only integers are allowed")
