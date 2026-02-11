# 🏥 Hospital Management System (OOP Project)

## 📌 Project Overview

This project is a Hospital Management System built using Object-Oriented Programming (OOP) in Python.

The system allows:
- Creating a hospital
- Adding departments
- Adding patients
- Adding staff members
- Viewing department details

This project demonstrates:
- Inheritance
- Class relationships
- Clean code organization
- Team collaboration using Git & GitHub

---

## 👥 Team Workflow

- Each member works on their own **feature branch**
- No direct push to `main`
- All changes must go through a **Pull Request**
- Team Lead reviews and merges

---

## 🌿 Branch Strategy

We are using the following branches:

- `feature-person-patient`
- `feature-staff`
- `feature-department`
- `feature-ui`
- `main` (protected branch)

Each member works only on their assigned branch.

---

## 📋 Task Distribution

### 👤 hakimy – Person & Patient  
Branch: `feature-person-patient`

Responsible for:
- `person.py`
- `patient.py`
- Implementing inheritance

---

### 👤 mohab – Staff  
Branch: `feature-staff`

Responsible for:
- `staff.py`
- Overriding methods properly

---

### 👤 Atef – Department  
Branch: `feature-department`

Responsible for:
- `department.py`
- Managing patients and staff lists

---

### 👤 Mostfa ayman – User Interface  
Branch: `feature-ui`

Responsible for:
- Menu system
- Handling user input
- Connecting classes inside `main.py`

---

###  Team Lead Nour mamdouh 
Branch: `main`

Responsible for:
- `hospital.py`
- Project integration
- Code review
- Final testing
- Merging Pull Requests

---

## 📁 Project Structure

```
hospital_system/
│
├── person.py
├── patient.py
├── staff.py
├── department.py
├── hospital.py
├── main.py
```

---

## 🧩 Starter Code Template

### person.py

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"
```

---

### patient.py

```python
from person import Person

class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        return f"Medical Record: {self.medical_record}"
```

---

### staff.py

```python
from person import Person

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"
```

---

### department.py

```python
class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
```

---

### hospital.py

```python
class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
```

---

## ⚠️ Project Rules

1. No `print()` inside class files.
2. All output must be handled inside `main.py`.
3. Each member works only on assigned files.
4. No direct push to `main`.
5. Every change must go through Pull Request.
6. Keep code clean and readable.

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📚 Future Improvements

- Add search functionality
- Add remove functionality
- Add unique IDs for patients and staff
- Add data saving using JSON
- Add proper error handling

---

### 🔥 Built with Python and OOP Principles
