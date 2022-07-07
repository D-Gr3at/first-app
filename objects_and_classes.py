class Person:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def print_data(self):
        print(self.name, self.age)


class Dog:
    name = 'Bingo'

    def print_name(self):
        print(f"The dog's name is: {self.name}")


if __name__ == '__main__':
    d = Dog()
    f = Dog()
    d.name = 'Luke'
    # del d
    # d.print_name()
    # f.print_name()

    p = Person('Israel', 'myemail@ymail.com', 19)

    print(p.name)

    q = Person('Hassan', 'hassan@gamil.com', 20)

    print(q.email)

    r = Person('Bille', '', 343)

    r.print_data()

    print(r.name)
