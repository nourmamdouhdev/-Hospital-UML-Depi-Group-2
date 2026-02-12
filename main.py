from Hospital import Hospital
from department import Department
from staff import Staff


def main():
    # Create Hospital
    hospital = Hospital("Cairo International Hospital")

    # Create Departments
    cardiology = Department(1)
    neurology = Department(2)

    # Add Departments to Hospital
    hospital.add_department(cardiology)
    hospital.add_department(neurology)

    # Create Staff
    doctor1 = Staff("Ahmed Ali", 40, "Doctor")
    nurse1 = Staff("Mona Samir", 28, "Nurse")

    # Add Staff to Departments
    cardiology.add_staff(doctor1)
    cardiology.add_staff(nurse1)

    # Show Data
    print(hospital)
    hospital.show_all_departments()

    print("\n--- Staff in Cardiology ---")
    for staff in cardiology.get_all_staff():
        print(staff.view_info())


if __name__ == "__main__":
    main()
