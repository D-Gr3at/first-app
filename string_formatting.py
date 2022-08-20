# To make sure a string will display as expected, we can format the result with the format() method.

if __name__ == '__main__':
    price = 49
    txt = "The price is {} dollars"
    print(txt.format(price))

    item_no = 45
    count = 2
    txt = "The price is {:.1f} dollars"
    print(txt.format(price, item_no, count))

    quantity = 3
    item_no = 567
    price = 49
    my_order = "I want {} pieces of item number {} for {:.2f} dollars."
    print(my_order.format(quantity, item_no, price))

    quantity = 3
    item_no = 567
    price = 49
    myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
    print(myorder.format(quantity, item_no, price))

    age = 36
    name = "John"
    txt = "His name is {1}. {1} is {3} years old."

    try:
        print(txt.format(age, name))
    except IndexError:
        print("An error occurred!!")

    myorder = "I have a {carname}, it is a {model}."
    print(myorder.format(carname="Ford", model="Mustang"))

