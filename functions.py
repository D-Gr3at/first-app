def print_message(name):
    print(f"Welcome {name} to discussing functions!")


def add(number1, number2):
    return number1 + number2


def my_fun():
    pass


def subtract(number1, number2):
    print(f"subtract = {number1 - number2}")


def cal_total(*data):
    if data == ():
        print("No value passed as argument")
    else:
        total = 0
        for x in data:
            total += x
        print(f"sum = {total}")


def list_names(**data):
    if data == {}:
        print("No value passed as argument")
    else:
        for value in data.values():
            print(value['name'])


def display_country(country="Nigeria"):
    print(country)


def my_list(data):
    if type(data) is list:
        if not data:
            print("List is empty")
        else:
            for number in data:
                print(number * 2)
    else:
        print("not a list")


if __name__ == '__main__':
    print_message("AdeJuwin")

    c = add(9, 87)
    print(f"sum = {c}")

    cal_total(6, 9, 3, 4, 10, 36)

    subtract(number2=90, number1=30)

    list_names(emp1={'name': 'Bille', 'salary': 7500}, emp2={'name': 'Israel', 'salary': 8005},
               emp3={'name': 'Katherine', 'salary': 5010})

    display_country("Norway")

    my_list("")
