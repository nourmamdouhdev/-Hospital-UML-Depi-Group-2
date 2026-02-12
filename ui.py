# interface.py

from staff import Staff
from department import Department
from hospital import Hospital

class Interface:
    """
    User interface for the hospital system.
    Handles input/output and connects Hospital, Department, and Staff classes.
    """

    def __init__(self, hospital_name: str):
        self.hospital = Hospital(hospital_name)

    # ---------------- Hospital Operations ---------------- #
    def add_department(self):
        """Prompt to add a new department to the hospital."""
        while True:
            try:
                dept_number = int(input(
                    "Enter department number (1-5):\n"
                    "1. Cardiology\n2. Neurology\n3. Pediatrics\n"
                    "4. Oncology\n5. Emergency\n"
                ))
                if dept_number not in range(1, 6):
                    raise ValueError
                department = Department(dept_number)
                self.hospital.add_department(department)
                print(f"Department {department.department_name()} added to hospital.")
                break
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")
            except TypeError as e:
                print(f"Error: {e}")

    def select_department(self):
        """Select a department already added to the hospital."""
        if not self.hospital.departments:
            print("No departments in the hospital. Please add a department first.")
            return None
        while True:
            try:
                dept_number = int(input("Enter department number to select: "))
                department = self.hospital.get_department(dept_number)
                if not department:
                    print("Department not found.")
                    continue
                return department
            except ValueError:
                print("Invalid input. Enter a number.")

    # ---------------- Patient Operations ---------------- #
    def input_patient(self, department: Department):
        name = input("Enter patient name: ")
        patient_id = int(input("Enter patient ID: "))
        department.add_patient(name, patient_id)
        print(f"Patient {name} added to {department.department_name()}.")

    def remove_patient(self, department: Department):
        patient_id = int(input("Enter patient ID to remove: "))
        department.remove_patient_by_id(patient_id)
        print(f"Patient with ID {patient_id} removed (if existed).")

    def view_patients(self, department: Department):
        patients = department.get_all_patients()
        if not patients:
            print("No patients in this department.")
            return
        print(f"\nPatients in {department.department_name()}:")
        for p in patients:
            print(f"Name: {p['name']}, ID: {p['id']}")

    # ---------------- Staff Operations ---------------- #
    def input_staff(self, department: Department):
        name = input("Enter staff name: ")
        age = int(input("Enter staff age: "))
        while True:
            position = input(
                "Enter staff position (Doctor, Nurse, Receptionist, Technician, Admin): "
            )
            try:
                staff_member = Staff(name, age, position)
                break
            except ValueError as e:
                print(f"Error: {e}")
        department.add_staff(staff_member.name, staff_member.position)
        print(f"Staff {staff_member.name} added to {department.department_name()}.")

    def remove_staff(self, department: Department):
        staff_id = input("Enter staff ID/position to remove: ")
        department.remove_staff_by_id(staff_id)
        print(f"Staff with ID/position {staff_id} removed (if existed).")

    def view_staff(self, department: Department):
        staff_list = department.get_all_staff()
        if not staff_list:
            print("No staff in this department.")
            return
        print(f"\nStaff in {department.department_name()}:")
        for s in staff_list:
            print(f"Name: {s['name']}, ID/Position: {s['id']}")

    # ---------------- Hospital Summary ---------------- #
    def view_hospital_info(self):
        print(f"\n{self.hospital}")
        self.hospital.show_all_departments()
        print(f"Total patients: {self.hospital.total_patients()}")
        print(f"Total staff: {self.hospital.total_staff()}")
