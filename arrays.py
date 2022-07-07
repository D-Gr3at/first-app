# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
if __name__ == '__main__':
    arr = ['blue', 'yellow', 'red']
    numbers = [10, 4, 0, 2, 9, 3, 6]
    # arr.extend(numbers)
    # print(arr)

    # append()	Adds an element at the end of the list
    arr.append('pink')
    # arr.clear()
    arr.insert(-2, 'Cyan')

    for el in arr:
        print(el)

    numbers.pop(3)
    #
    print(numbers)
    #
    # arr.remove('yellow')
    # #
    # numbers.sort(reverse=True)
    # print(arr.count('red'))


