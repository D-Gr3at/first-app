if __name__ == '__main__':
    # for loops
    for x in [2, 4, 6, 8, 10]:
        product = x*2
        if product > 12:
            continue
        if x == 4:
            product = x*3
        print(product)

    for count in range(0, 10, 2):
        print(count)

    # while loops
    b = 10
    while b > 0:
        print(b)
        if b == 6:
            break
        b -= 1
    else:
        print("Failed!")

    for x in ("Blue", "City", 23, True):
        print(x)

    for c in range(12, 0, -1):
        print(c)
