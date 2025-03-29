# Example explained:
# In our example, Employee, Developer, and Manager are all different types, 
# but they share common methods (calculate_bonus() and display_info()). 
# The print_employee_details() function works with any employee type without needing to know the specific class. 
# When it calls employee.calculate_bonus(), the appropriate version of the method is executed based on the actual object type.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.1
        
    def display_info(self):
        return f"{self.name}'s annual salary is ${self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def calculate_bonus(self):
        return self.salary * 0.15  # Developers get a higher bonus
    
    def display_info(self):
        return f"{self.name} is a {self.programming_language} developer with salary ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def calculate_bonus(self):
        return self.salary * 0.2 + 100 * self.team_size  # Managers get bonus based on team size too
    
    def display_info(self):
        return f"{self.name} manages {self.team_size} employees with salary ${self.salary}"

# Function demonstrating polymorphism
def print_employee_details(employee_list):
    for employee in employee_list:
        print(employee.display_info())
        print(f"Bonus: ${employee.calculate_bonus()}")
        print("---")

# Create different types of employees
employees = [
    Employee("Alice", 50000),
    Developer("Bob", 70000, "Python"),
    Manager("Charlie", 90000, 8)
]

# All are treated as employees even though they're different types
print_employee_details(employees)