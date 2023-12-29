import mymodule as mx
import platform


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.modle = model
        self.brand = brand

    def move(self):
        print("Sail")


class Plane(Car, Boat):
    def __init__(self, brand, model):
        self.modle = model
        self.brand = brand

    def move(self):
        print("Fly")


car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "737")

plane.move()


for x in (car, boat, plane):
    x.move()

# mx.greeting("Kumari Sekhar")
# a = mx.person1["age"]
# print("Age : ", a)
# x = platform.system()
# print(x)
# x = dir(platform)
# print(x)
# processor_value = platform._Processor if hasattr(platform, '_Processor') else None
# print("Processor Value:", processor_value)
