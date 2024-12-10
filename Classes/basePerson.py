class Person:

    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def print_self(self):
        print(f"{self.firstname} {self.lastname}, Age: {self.age}")

