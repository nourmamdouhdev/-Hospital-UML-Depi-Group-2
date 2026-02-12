class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        return "Name: " + self.name + " | Age: " + str(self.age)
