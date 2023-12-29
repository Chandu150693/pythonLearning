class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class GVPPerson:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

class Student(Person,GVPPerson):
    def __init__(self, fname, lname, year):
        # super.__init__(fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome ", self.fname, self.lname, " to the class of ", self.graduationyear)


x = Student("Kumari", "Sekhar", 2018)
x.printname()
x.welcome()
