class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 30000)

if e1 > e2:
    print(f"{e1.name} earns more than {e2.name}")