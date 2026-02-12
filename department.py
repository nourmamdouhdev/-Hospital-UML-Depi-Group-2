from staff import Staff

class Department:
    def __init__(self, number):
        self.number = number
        self.patients = []
        self.staff = []

    # ---------------- Add ---------------- #
    def add_patient(self, patient):
        self.patients.append(patient)

    def add_staff(self, staff_member):
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
        return self.patients

    def display_patients(self):
        if not self.patients:
            print("No patients in this department.")
            return

        for p in self.patients:
            print(f"Name: {p['name']}, ID: {p['id']}")

    # ---------------- String ---------------- #
    def __str__(self):
        return (
            f"Department: {self.department_name()}, "
            f"Patients: {len(self.patients)}, "
            f"Staff: {len(self.staff)}"
        )

    def remove_staff_by_id(self, staff_id):
        for s in self.staff:
            if s.id == staff_id:
                self.staff.remove(s)
                return True
        return False
        
    def display_staff(self):
        if not self.staff:
            print("No staff in this department.")
            return

        for s in self.staff:
            print(s.view_info())

    def get_all_staff(self):
        return self.staff