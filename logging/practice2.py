import logging

logging.basicConfig(filename="employee_creation.log", level=logging.INFO, format='%(asctime)s:%(filename)s:%(lineno)d:%(message)s') 



class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department
        logging.info(f"Employee created: {self.name}, Department: {self.department}")

employee1=Employee("Preetam", "Product")
employee2=Employee("Aditya", "AI")
employee3=Employee("Anika", "Product")

