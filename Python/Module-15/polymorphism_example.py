class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Designer(Employee):
    def work(self):
        print("Designer is creating UI")


employees = [Developer(), Designer()]

for employee in employees:
    employee.work()