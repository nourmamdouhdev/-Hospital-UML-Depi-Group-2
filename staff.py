from person import Person


class Staff(Person):
    """
    Represents a hospital staff member.
    Inherits basic attributes from Person.
    """
    # Allowed job positions in the system
    VALID_POSITIONS = {"Doctor", "Nurse", "Receptionist", "Technician", "Admin"}

    def __init__(self, name, age, position):
        """
        Constructor for Staff class.
        Parameters:
        name (str): Staff member's name
        age (int): Staff member's age
        position (str): Staff member's job position
        """
        # Call Person constructor to initialize name and age
        super().__init__(name, age)

        # Validate and assign position
        self.position = self._validate_position(position)

    def _validate_position(self, position):
        """
        Validates the staff position.
        Rules:
        - Must be a string
        - Cannot be empty
        - Must be one of VALID_POSITIONS
        """
        # Check if position is a string
        if not isinstance(position, str):
            raise ValueError("Position must be a string.")
        # Clean input (remove spaces & standardize format)
        cleaned_position = position.strip().title()
        
        # Check if position is empty
        if not cleaned_position:
            raise ValueError("Position cannot be empty.")

        # Check if position is allowed
        if cleaned_position not in self.VALID_POSITIONS:
            allowed = ", ".join(self.VALID_POSITIONS)
            raise ValueError(f"Invalid position. Allowed positions: {allowed}")

        return cleaned_position

    def view_info(self):
        """
        Returns formatted staff information.

        Overrides Person.view_info()
        """

        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"
