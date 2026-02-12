class Person:
    def __init__(self, name, age,position):
        self.name = name
        self.age = age
        self.position = position
    def view_info(self):
        return "Name: " + self.name + " | Age: " + str(self.age)
