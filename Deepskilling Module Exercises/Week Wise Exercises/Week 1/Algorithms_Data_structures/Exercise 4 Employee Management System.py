class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

employees = []

def add_employee(emp):
    employees.append(emp)

def search_employee(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp
    return None

def delete_employee(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("Employee Deleted")
            return

add_employee(Employee(1, "Vaibhav", "Developer", 50000))
add_employee(Employee(2, "Rahul", "Tester", 40000))

for emp in employees:
    print(emp.name)

delete_employee(1)
