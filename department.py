##___________________CLASS DEPARTMENT______________________##

class Department:
    """
    Represents a department in the hospital, managing patients and staff.
    """

    def __init__(self, number):
        """Initializes a Department instance with the given number."""
        self.number = number
        self.patients = []
        self.staff = []

    # ---------------- Add ---------------- #

    def add_patient(self, patient, patient_id):
        """Adds a patient to the department."""
        self.patients.append(patient)
        self.patients.append(patient_id)

    def add_staff(self, staff_member, member_id):
        """Adds a staff member to the department."""
        self.staff.append(staff_member)
        self.staff.append(member_id)

    # ---------------- Department Name ---------------- #

    def department_name(self):
        """Returns the department name based on its number."""
        departments = {
            1: "Cardiology",
            2: "Neurology",
            3: "Pediatrics",
            4: "Oncology",
            5: "Emergency"
        }
        return departments.get(self.number, "Invalid department number")

    # ---------------- Get ---------------- #

    def get_all_patients(self):
        """Returns a list of all patients."""
        return self.patients

    def get_all_staff(self):
        """Returns a list of all staff members."""
        return self.staff

    # ---------------- Remove ---------------- #

    def remove_patient(self, patient, patient_id):
        """Removes a patient using name and ID."""
        if patient in self.patients:
            index = self.patients.index(patient)
            self.patients.pop(index)
            self.patients.pop(index)

    def remove_staff(self, staff_member, member_id):
        """Removes a staff member using name and ID."""
        if staff_member in self.staff:
            index = self.staff.index(staff_member)
            self.staff.pop(index)
            self.staff.pop(index)

    # ---------------- String ---------------- #

    def __str__(self):
        return (
            f"Department: {self.department_name()}, "
            f"Patients: {len(self.patients)//2}, "
            f"Staff: {len(self.staff)//2}"
        )
