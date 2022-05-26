if __name__ == '__main__':
    my_tuple = ("green", "yellow", "blue")
    print(my_tuple)  # ordered and unchangeable - can't add, remove or change item

    # tuple with one item
    one_tuple = ("black",)

    print(type(one_tuple))

    # allows duplicate
    one_tuple = ("Uruguay", "Brasil", "Uruguay")
    print(one_tuple)

    # length of a tuple
    print(len(my_tuple))

    # tuple with multiple data types
    data_types = (True, "String", 34)
    print(type(data_types))

    # make tuple
    make_tuple = tuple(("white", "red", "pink", "violet", "brown", "green", "blue", "orange"))
    print(make_tuple)

    # Accessing a tuple
    print(make_tuple[1])
    print(make_tuple[2:])
    print(make_tuple[:4])
    print(make_tuple[2:4])

    # if check
    if "White" in make_tuple:
        print("White is present.")

    # update tuple
    y = ("indigo",)
    make_tuple += y
    print(make_tuple)

    y = list(make_tuple)
    y.append("lemon")
    make_tuple = tuple(y)
    print(make_tuple)

    # unpacking tuples
    colors = ("yellow", "white", "red")  # packing
    (james, linda, smith) = colors  # unpacking
    print(james)
    print(linda)
    print(smith)

    # using asterisks
    (james, linda, *smith) = make_tuple
    print(smith)

    # looping
    for item in make_tuple:
        print(item)

    # while loop
    count = 0
    while count < len(make_tuple):
        print(make_tuple[count])
        count += 1

    # for range
    for j in range(len(make_tuple)):
        print(make_tuple[j])







