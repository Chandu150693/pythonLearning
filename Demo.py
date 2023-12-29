class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def myfunc(self):
        print("Hello my name is : ", self.name)


p = Person("Chandu", 30)
p1 = Person("Kumari", 22)
# print(p.name, " is ", p.age, " years old.")
# print(p1.name, " is ", p1.age, " years old.")

# print(p)
# print(p1)
p1.myfunc()


class TestObject:
    def __init__(sillyobj, name, age):
        sillyobj.name = name
        sillyobj.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


myObj = TestObject("Chandu", 30)
print(myObj)

p1.age = 23

print(p1)
del p1
print("p1 obj deleted")
print(p1)