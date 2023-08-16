class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def display(self):
        print(f"Instance value: {self.value}")
        print(f"Class variable: {self.class_variable}")

# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Accessing class method
obj1.increment_class_variable()

# Calling instance methods
obj1.display()
obj2.display()
