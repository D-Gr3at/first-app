# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):  # constructor
        self.first_name = fname
        self.last_name = lname

    def print_details(self):
        print(self.first_name, self.last_name)


class Student(Person):
    # pass
    def __init__(self, fname, lname, s_id):
        super().__init__(fname, lname)
        self.student_id = s_id

    def print_details(self):
        print(self.first_name, self.last_name, self.student_id)


if __name__ == '__main__':
    # p = Person()
    s = Student("Sarah", "Doe", "H0008657")
    s.print_details()

