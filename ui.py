# interface.py
from staff import Staff
from department import Department
from Hospital import Hospital

class Interface:
    """
    User interface for the hospital system.
    Works with the existing Department, Staff, and Hospital classes.
    """

    def __init__(self, hospital_name: str):
        self.hospital = Hospital(hospital_name)

    # ---------------- Hospital Operations ---------------- #
    def add_department(self):
        try:
            dept_number = int(input(
                "Enter department number (1-5):\n"
                "1. Cardiology\n2. Neurology\n3. Pediatrics\n"
                "4. Oncology\n5. Emergency\n"
            ))
            if dept_number not in range(1, 6):
                print("Invalid number")
                return
            department = Department(dept_number)
            self.hospital.add_department(department)
            print(f"Department {department.department_name()} added.")
        except ValueError:
            print("Please enter a valid number.")

    def select_department(self):
        if not self.hospital.departments:
            print("No departments added yet.")
            return None
        try:
            dept_number = int(input("Enter department number to select: "))
        except ValueError:
            print("Invalid input")
            return None
        department = self.hospital.get_department(dept_number)
        if not department:
            print("Department not found.")
        return department

    # ---------------- Patient Operations ---------------- #
    def input_patient(self, department: Department):
        name = input("Enter patient name: ")
        patient_id = input("Enter patient ID: ")

        patient = {"name": name, "id": patient_id}
        department.add_patient(patient)
        print(f"Patient {name} added.")

    def remove_patient(self, department: Department):
        patient_id = input("Enter patient ID to remove: ")
        patients = department.get_all_patients()
        for p in patients:
            if p["id"] == patient_id:
                patients.remove(p)
                print(f"Patient with ID {patient_id} removed.")
                return
        print("Patient not found.")

    def view_patients(self, department: Department):
        patients = department.get_all_patients()
        if not patients:
            print("No patients in this department.")
            return
        print(f"Patients in {department.department_name()}:")
        for p in patients:
            print(f"Name: {p['name']}, ID: {p['id']}")

    # ---------------- Staff Operations ---------------- #
    def input_staff(self, department: Department):
        name = input("Enter staff name: ")
        try:
            age = int(input("Enter staff age: "))
        except ValueError:
            print("Age must be a number")
            return
        position = input("Enter staff position (Doctor, Nurse, Receptionist, Technician, Admin): ")
        try:
            staff_member = Staff(name, age, position)
        except ValueError as e:
            print(f"Error: {e}")
            return
        department.add_staff(staff_member)
        print(f"Staff {name} added.")

    def remove_staff(self, department):
        staff_id = int(input("Enter staff ID to remove: "))
        removed = department.remove_staff_by_id(staff_id)
        if removed:
            print(f"Staff with ID {staff_id} removed.")
        else:
            print("Staff not found.")

    def view_staff(self, department: Department):
        staff_list = department.get_all_staff()
        if not staff_list:
            print("No staff in this department.")
            return
        print(f"Staff in {department.department_name()}:")
        for s in staff_list:
            print(s.view_info())

    # ---------------- Hospital Summary ---------------- #
    def view_hospital_info(self):
        print(f"\n{self.hospital}")
        self.hospital.show_all_departments()
        print(f"Total patients: {self.hospital.total_patients()}")
        print(f"Total staff: {self.hospital.total_staff()}")
