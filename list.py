if __name__ == '__main__':

    another_list = []  # empty list
    # List
    my_list = ["Netherlands", "argentina", "England", "Russia"]
    print(f"Actual List = {my_list}")

    # Accessing List item by index
    first_item = my_list[0]
    print(f"first item = {first_item}")

    sub_list = my_list[1:3]
    print(f"Sub List = {sub_list}")

    # negative index
    print(f"Last item = {my_list[-1]}")
    print(f"Second Last item = {my_list[-2]}")

    # Updating List by index
    my_list[2] = "Red Hat"
    print(f"new updated list = {my_list}")

    my_list[0:2] = ["Ubuntu", "Kali", "Neo"]
    print(f"new updated list = {my_list}")

    # Adding items to list
    my_list.append("Bodhi")
    print(f"Added element = {my_list}")

    my_list.insert(-1, "Parrot")
    print(f"Added element = {my_list}")

    # Removing from list
    my_list.remove("Red Hat")
    print(f"My list = {my_list}")

    my_list.pop(0)
    print(f"My list = {my_list}")

    # Looping through list:
    for item in my_list:
        print(item)

    print("==============================")

    for i in range(len(my_list)):
        print(my_list[i])

    print("==============================")

    i = 0
    while i < len(my_list):
        print(my_list[i])
        i = i + 1

    print("==============================")

    [print(item) for item in my_list]

    # Sort list - alphanumerically, ascending
    my_list.sort()
    print(my_list)

    my_list.sort(reverse=True)  # descending order
    print(my_list)

    my_list.sort(key=str.lower)
    print(my_list)

    my_list.reverse()  # reverse list
    print(my_list)

    # Copying list
    list_copy = my_list.copy()
    print(list_copy)

    list_copy = list(my_list)
    print(list_copy)

    # Join two lists
    first_list = ["Java", "Golang", "Play"]
    second_list = ["Python", "PHP", "JavaScript"]
    programming_languages = first_list + second_list
    print(programming_languages)

    first_list.extend(second_list)
    print(first_list)

    main_list = [0, 1, 2]
    for item in second_list:
        main_list.append(item)
    print(first_list)



