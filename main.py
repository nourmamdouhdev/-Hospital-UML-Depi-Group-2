# main.py
from ui import Interface

def main():
    print("Welcome to Cairo International Hospital System!\n")
    ui = Interface("Cairo International Hospital")

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Department")
        print("2. Select Department")
        print("3. View Hospital Info")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ui.add_department()

        elif choice == "2":
            dept = ui.select_department()
            if not dept:
                continue

            while True:
                print(f"\n--- Department: {dept.department_name()} ---")
                print("1. Add Patient")
                print("2. Remove Patient")
                print("3. View Patients")
                print("4. Add Staff")
                print("5. Remove Staff")
                print("6. View Staff")
                print("7. Back to Main Menu")

                dep_choice = input("Enter your choice: ")

                if dep_choice == "1":
                    ui.input_patient(dept)
                elif dep_choice == "2":
                    ui.remove_patient(dept)
                elif dep_choice == "3":
                    ui.view_patients(dept)
                elif dep_choice == "4":
                    ui.input_staff(dept)
                elif dep_choice == "5":
                    ui.remove_staff(dept)
                elif dep_choice == "6":
                    ui.view_staff(dept)
                elif dep_choice == "7":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "3":
            ui.view_hospital_info()

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
