class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive value")

# Creating an object
person = Person("Alice", 30)

# Using getter and setter methods
print("Name:", person.get_name())
person.set_name("Bob")
print("Name:", person.get_name())

print("Age:", person.get_age())
person.set_age(-25)
print("Age:", person.get_age())
