##___________________CLASS DEPARTMENT______________________##

class Department:

    """Represents a department in the hospital, managing patients and staff.
    Attributes:

        number (int): The number of the department.
        1. Cardiology
        2. Neurology
        3. Pediatrics
        4. Oncology
        5. Emergency

        patients (list): A list of patients in the department.

        staff (list): A list of staff members in the department.

    """


    #-----------------------------------------------------#


    def __init__(self, number):
        '''Initializes a Department instance with the given number and empty lists for patients and staff.'''
        self.number = number
        self.patients = []
        self.staff = []

    def add_patient(self, patient , patient_id):
        """Adds a patient to the department"""
        self.patients.append(patient)
        self.patients.append(patient_id)

    def add_staff(self, staff_member , member_id):
        """Adds a staff member to the department"""
        self.staff.append(staff_member)
        self.staff.append(member_id)


    ##------------------------Know department Name----------------------------##


    def Department_name(self):
        """
        Returns :

        the name of the department based on its number.
        """
        if self.number == 1:
            return "Cardiology"
        elif self.number == 2:
            return "Neurology"
        elif self.number == 3:
            return "Pediatrics"
        elif self.number == 4:
            return "Oncology"
        elif self.number == 5:
            return "Emergency"
        else:
            return "Invalid department number"
            pass

##------------------------Input patient and staff----------------------------##

    def input_patient(self):
        """
        Prompts the user to input patient information and adds the patient to the department.
        """
        patient= input("Enter patient name: ")
        patient_id= int(input("Enter patient ID: "))
        self.add_patient(patient, patient_id)

        
    def input_Staff(self):
        """
        Prompts the user to input staff member information and adds the staff member to the department."""
        staff_member= input("Enter staff member name: ")
        member_id= int(input("Enter staff member ID: "))
        self.add_staff(staff_member, member_id)

    def get_all_patients(self):
        """
        Returns a list of all patients in the department.
        """
        return self.patients
    
    def get_all_staff(self):
         """
        Returns a list of all staff members in the department.
         """
         return self.staff
    
##------------------------Remove patient and staff----------------------------##


    def remove_patient(self, patient ,patient_id):
        """
        Removes a patient from the department by its ID only.

        """
        if patient in self.patients:
            index = self.patients.index(patient)
            self.patients.pop(index)
            self.patients.pop(index)
            
    def remove_staff(self, staff_member ,member_id):
        """
        Removes a staff member from the department by its ID only.
        """
        if staff_member in self.staff:
            index = self.staff.index(staff_member)
            self.staff.pop(index)
            self.staff.pop(index)
    def input_remove_patient(self):
        """
        Prompts the user to input a patient ID and removes the corresponding patient from the department.
        """
        patient_id= int(input("Enter patient ID to remove: "))
        if patient_id in self.patients:
            index = self.patients.index(patient_id)
            patient = self.patients[index - 1]  # Assuming patient name is before ID
        else:
            print("Patient ID not found.")
            return
        self.remove_patient(patient, patient_id)
    
    def input_remove_staff(self):
        """
        Prompts the user to input a staff member ID and removes the corresponding staff member from the department.
        """
        member_id= int(input("Enter staff member ID to remove: "))
        if member_id in self.staff:
            index = self.staff.index(member_id)
            staff_member = self.staff[index - 1]  # Assuming staff member name is before ID
        else:
            print("Staff member ID not found.")
            return
        self.remove_staff(staff_member, member_id)

    def __str__(self):
        """
        Returns a string representation of the department, including its name, number of patients, and number of staff members.
        """
        return f"Department: {self.Department_name()}, Patients: {len(self.patients) // 2}, Staff: {len(self.staff) // 2}"


##_______________________TEST FOR CLASS__________________________##
#

import sys
dept_number = input("Enter department id: \n" \
"1. Cardiology\n" \
"2. Neurology\n" \
"3. Pediatrics\n" \
"4. Oncology\n" \
    "5. Emergency\n" )
import sys

dept_number = input("Enter department id: \n" \
"1. Cardiology\n" \
"2. Neurology\n" \
"3. Pediatrics\n" \
"4. Oncology\n" \
"5. Emergency\n" )

if dept_number.isdigit():
    dept_number = int(dept_number)
    if 1 <= dept_number <= 5:
        dep = Department(dept_number)  # كائن واحد فقط
    else:
        print("Wrong department number! Program will stop.")
        sys.exit()
else:
    print("Please enter a valid integer! Program will stop.")
    sys.exit()

dep.input_patient()
print(dep.get_all_patients())
dep.input_patient()
print(dep.get_all_patients())
dep.input_patient()
print(dep.get_all_patients())
dep.input_Staff()
print(dep.get_all_staff())
dep.input_remove_patient()
print(dep.get_all_patients())
dep.input_remove_staff()
print(dep.get_all_staff())
print(dep)
