if __name__ == '__main__':
    my_set = {"Kelvin", "Logan", "Scot", "Desmond"}
    data_set = {"string", 123, True, False}
    colors = {"black", "white", "blue", "grey", "pink", "black"}

    print(colors)

    # add to set
    colors.add("red")
    colors.update(my_set)

    # remove
    colors.remove("black")
    colors.discard("black")

    # accessing set - it must be converted to a list
    print(list(my_set))

    # loop
    for x in colors:
        print(x)

    counter = len(my_set) - 1
    while counter >= 0:
        print(list(my_set)[counter])
        counter -= 1
