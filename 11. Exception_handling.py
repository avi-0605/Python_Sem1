# #1
# x=10
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     print("The result is:", numerator/denominator)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter valid numbers.")

# try:
#     num=int(input("Enter an integer: "))
#     print("You entered:",num)
# except ValueError:
#     print("Error: That is not a valid integer.")

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input, please enter integers.")
# except Exception as e:
#     print("An unexpected error occurred:", e)

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     print("Result:", result)
# except (ZeroDivisionError, ValueError) as e:
#     print("Error:", e)