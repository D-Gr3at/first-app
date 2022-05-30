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

    #   union - joint two sets
    x = {1, 2, 3, 4, 5}
    y = {"a", "b", "c", "d", "e"}

    z = x.union(y)
    print("z = ", z)
    x.update(y)
    print("x = ", x)

    #     intersect - keep only duplicates
    x.intersection_update(y)
    print("intersection (x n y) = ", x)

    intersect = z.intersection(x)
    print("intersection (z n x) = ", intersect)

    #     symmetric difference
    z.symmetric_difference_update(x)
    print("symmetric difference update = ", z)

    symmetric_difference = y.symmetric_difference(x)
    print("symmetric difference = ", symmetric_difference)
