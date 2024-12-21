# # 1. Write a Python class that has two methods: get_String and print_String , get_String
# # accept a string from the user and print_String prints the string in upper case.
# class StringHandler:
#     def __init__(self):
#         s.input_string = ""

#     def g_string(self):
#         s.input_string = input("Enter string: ")

#     def print_string(self):
#         print(s.input_string.upper())


# # 2. Write a Python program to create a calculator class. Include methods for basic
# # arithmetic operations.
# class Calculator:
#     def add(self, x, y):
#         return x + y

#     def subtract(self, x, y):
#         return x - y

#     def multiply(self, x, y):
#         return x * y

#     def divide(self, x, y):
#         return x / y if y != 0 else "Can't divide by zero"



# # 3. Write a Python class named Circle constructed from a radius and two methods that
# # will compute the area and the perimeter of a circle.
# import math

# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# # 4. Write a Python class to implement pow(x, n).
# class Pow:
#     def pow(x, n):
#         return x ** n



# # 5. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, item, price):
#         if item in self.items:
#             self.items[item] += price
#         else:
#             self.items[item] = price

#     def remove_item(self, item):
#         if item in self.items:
#             del self.items[item]

#     def total_price(self):
#         return sum(self.items.values())


# # 6. Write a Python class Employee with attributes like emp_id, emp_name,
# class Employee:
#     def __init__(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department

#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked > 50:
#             overtime = hours_worked - 50
#             overtime_amount = (overtime * (self.emp_salary / 50))
#             return self.emp_salary + overtime_amount
#         return self.emp_salary

#     def assign_department(self, new_department):
#         self.emp_department = new_department

#     def print_employee_details(self):
#         print(f"ID: {self.emp_id}, Name: {self.emp_name}, Salary: {self.emp_salary}, Department: {self.emp_department}")


# # 7. Write a  Python class BankAccount with attributes like account_number, balance,
# # date_of_opening and customer_name, and methods like deposit, withdraw, and
# # check_balance.
# class Bank:
#     def __init__(self, acc_number, cust_name, balance=0, date_of_opening=None):
#         self.acc_number = account_number
#         self.cust_name = customer_name
#         self.balance = balance
#         self.date_of_opening = date_of_opening

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")

#     def check_balance(self):
#         return self.balance

# #8.Create a class hierarchy for different types of geometric shapes, including circles,rectangles, and triangles, using inheritance.
# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius, color):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, base, height, color):
#         super().__init__(color)
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# # 9. Create a Bus child class that inherits from the Vehicle class. The default fare charge of
# class Vehicle:
#     def __init__(self, seating_capacity):
#         self.seating_capacity = seating_capacity

#     def fare(self):
#         return self.seating_capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         base_fare = super().fare()
#         maintenance_charge = base_fare * 0.10
#         return base_fare + maintenance_charge