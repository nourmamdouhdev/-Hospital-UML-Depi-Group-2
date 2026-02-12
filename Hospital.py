
##___________________CLASS HOSPITAL______________________##

from department import Department


class Hospital:
    """
    Represents a hospital that manages multiple departments.
    """

    def __init__(self, name):
        self.name = name
        self.departments = {}

    # ---------------- Add Department ---------------- #

    def add_department(self, department):
        """
        Adds a Department object to the hospital.
        """
        if not isinstance(department, Department):
            raise TypeError("Must be a Department object.")

        self.departments[department.number] = department

    # ---------------- Get Department ---------------- #

    def get_department(self, number):
        """
        Returns a department by its number.
        """
        return self.departments.get(number)

    # ---------------- Show All Departments ---------------- #

    def show_all_departments(self):
        """
        Prints all departments.
        """
        for dept in self.departments.values():
            print(dept)

    # ---------------- Hospital Statistics ---------------- #

    def total_patients(self):
        """
        Returns total number of patients in the hospital.
        """
        return sum(len(dept.patients) // 2 for dept in self.departments.values())

    def total_staff(self):
        """
        Returns total number of staff members in the hospital.
        """
        return sum(len(dept.staff) for dept in self.departments.values())

    # ---------------- String ---------------- #

    def __str__(self):
        return f"Hospital: {self.name}, Departments: {len(self.departments)}"
