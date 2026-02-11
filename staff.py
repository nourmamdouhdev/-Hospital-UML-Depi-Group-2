from person import Person


class Staff(Person):
    VALID_POSITIONS = {"Doctor", "Nurse", "Receptionist", "Technician", "Admin"}

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = self._validate_position(position)

    def _validate_position(self, position):
        if not isinstance(position, str):
            raise ValueError("Position must be a string.")

        cleaned_position = position.strip().title()

        if not cleaned_position:
            raise ValueError("Position cannot be empty.")

        if cleaned_position not in self.VALID_POSITIONS:
            allowed = ", ".join(self.VALID_POSITIONS)
            raise ValueError(f"Invalid position. Allowed positions: {allowed}")

        return cleaned_position

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"
