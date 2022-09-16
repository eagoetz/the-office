from collections import defaultdict
from typing import Set

from employee import Employee


class TheOffice:
    """Class about the office with manager, employee, sales, etc.

    Args:
        regional_manager (str): The name of the regional manager
        employees (Set[Employee]): set of employees
        location (str): location of the office
    """

    def __init__(self, regional_manager: str, employees: Set[Employee], location: str):
        self.regional_manager = regional_manager
        self.employees = employees
        self.location = location
        self.sales = defaultdict(int)

    def __str__(self) -> str:
        """Class as a string that prints the splash and who is the regional
        manager

        Returns:
            str: Welcome message
        """

        return f"Welcome to The Office! The boss here is {self.regional_manager}."

    def record_sale(self, employee: Employee) -> None:
        """Increment an employee sale

        Args:
            employee (Employee): The employee who made the sale
        """

        self.sales[employee] += 1

    def get_employee_sales(self, employee: Employee) -> int:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """

        return self.sales[employee]

    def _fire_employee(self, employee: Employee) -> None:
        """Remove an employee from set of employees.

        Args:
            employee (Employee): The employee to be removed
        """

        self.employees.remove(employee)
