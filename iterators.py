# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
# methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an
# iterator from. All these objects have a iter() method which is used to get an iterator:

class MyNumbers:
    def __init__(self, na):
        self.name = na;

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1  # -=, /=, *= --- compound operators.
            return x
        else:
            raise StopIteration


# if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration


if __name__ == '__main__':
    mytuple = ("Crotia", "India", "Canada")
    myit = iter(mytuple)

    # print(next(myit))
    # print(next(myit))
    # print(next(myit))

    # # String Iterator
    mystr = "Nigeria"
    myit = iter(mystr)

    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))

    # # Using for..in
    # for x in mytuple:
    #     print(x)
    #
    # for x in mystr:
    #     print(x)
    #
    # # Iterable Object
    myclass = MyNumbers()
    myiter = iter(myclass)
    #
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))

    # myclass = MyNumbers()
    # myiter = iter(myclass)
    #
    for x in myiter:
        print(x)
