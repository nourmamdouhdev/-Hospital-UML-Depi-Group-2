from staff import Staff

class Department:
    def __init__(self, number):
        self.number = number
        self.patients = []
        self.staff = []

    # ---------------- Add ---------------- #
    def add_patient(self, patient):
        """Adds a Patient object to the department."""
        self.patients.append(patient)

    def add_staff(self, staff_member):
        """Adds a Staff object to the department."""
        if isinstance(staff_member, Staff):
            self.staff.append(staff_member)
        else:
            raise ValueError("Must provide a Staff object")

    # ---------------- Department Name ---------------- #
    def department_name(self):
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
        """Returns formatted info of all patients."""
        return [p.view_info() for p in self.patients]

    def get_all_staff(self):
        return self.staff  # ترجع Staff objects مباشرة

    # ---------------- String ---------------- #
    def __str__(self):
        return (
            f"Department: {self.department_name()}, "
            f"Patients: {len(self.patients)}, "
            f"Staff: {len(self.staff)}"
        )
