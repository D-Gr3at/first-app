def my_sort(number):
    return abs(number - 50)


if __name__ == '__main__':
    my_list = [60, 0, 30, 100, 35, 80, 77, 19, 27, 90]
    my_list.sort(key=my_sort)
    print(my_list)


