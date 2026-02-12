# staff.py
from Person import Person

class Staff(Person):
    VALID_POSITIONS = {"Doctor", "Nurse", "Receptionist", "Technician", "Admin"}
    _id_counter = 1  # auto-increment ID for each staff

    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self.id = Staff._id_counter  # ID تلقائي لكل staff
        Staff._id_counter += 1
        self.position = self._validate_position(position)
        
    def _validate_position(self, position):
        cleaned_position = position.strip().title()
        if cleaned_position not in self.VALID_POSITIONS:
            allowed = ", ".join(self.VALID_POSITIONS)
            raise ValueError(f"Invalid position. Allowed: {allowed}")
        return cleaned_position

    def view_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Position: {self.position}"
