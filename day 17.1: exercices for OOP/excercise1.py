#Create a class named employee and initialize it with an attribute named employee
#create a method to change the default name
#create a new object and user the employee attribute


class Employee:
    def __init__(self) -> None:
        self.employee = 'default'


    def change_name(self, employee_name):
        self.employee = employee_name

    def __str__(self) -> str:
        return self.employee


new_employee = Employee()
print(new_employee)

new_employee.change_name('Jorge')
print(new_employee)
