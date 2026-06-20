class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)


p1 = Person("Ali", 25)

p1.say_hello()

print(p1.age)
