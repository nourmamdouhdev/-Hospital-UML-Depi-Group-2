# patient.py
from Person import Person

class Patient(Person):
    _id_counter = 1  # ID auto-increment

    def __init__(self, name, age):
        super().__init__(name, age)
        self.id = Patient._id_counter
        Patient._id_counter += 1

    def view_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"
