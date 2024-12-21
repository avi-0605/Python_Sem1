# 1. Write a program to check whether an years is leap year or not.
# n=int(input("Enter year:"))
# if (n%4==0 and n%100!=0) or (n%400==0):
#   print("It is a leap year ")
# else:
#   print("It is not a leap year.")


# 2. Write a program to check whether a number entered is three digit number or not.
# n=int(input("Enter a number :"))
# if n>100 or n<1000:
#   print("It is a three digit number .")
# else :
#   print("It is not a three digit number .")



# 3. Write a program to check whether a person is eligible for voting or not.(voting age
# &gt;=18)
# n=int(input("Enter your age :"))
# if n>18:
#   print("You are eligible to vote .")
# else:
#   print("You are not eligible to vote .")



# 4. Write a program to check whether the last digit of a number( entered by user ) is
# by 3.
# n=int(input("Enter a number:"))
# ld=n%10
# if ld==3:
#   print("Last digit is three:")
# else:
#   print("Last digit is not three:")


# 5. Write a Python program to check whether an alphabet is a vowel or consonant.
# n=str(input("Enter an alphabet"))
# if (n=="A" or n=="E" or n=="I" or n=="O" or n=="U" or n=="a"or n=="e" or n=="i" or n=="o"or n=="u"):
#   print("It is a vowel")
# else:
#   print("It is a consonant")


# 6. Write a Python program to convert a month name to a number of days.
# month_days = {
#     "January": 31,
#     "February": 28,
#     "March": 31,
#     "April": 30,
#     "May": 31,
#     "June": 30,
#     "July": 31,
#     "August": 31,
#     "September": 30,
#     "October": 31,
#     "November": 30,
#     "December": 31
# }
# month_name = input("Enter a month name: ")
# if month_name in month_days:
#     num_days = month_days[month_name]
#     print(f"The month of {month_name} has {num_days} days.")
# else:
#     print("Invalid month name.")


# 7. Write a Python program to check if a triangle is equilateral, isosceles or scalene. 
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# n=int(input("Enter side of triangle :"))
# m=int(input("Enter side of triangle:"))
# r=int(input("Enter side of tringle :"))
# if n==m==r:
#   print("It is an equilateral triangle .")
# elif n==m or n==r or m==r :
#   print("It is an isosceles triangle.")
# else: print("It is a scalene triangle .")



# 8. Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
# Unit Price
# First 100 units no charge
# Next 100 units Rs 5 per unit
# After 200 units Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs 2000)
# n=int(input("Enter the number of unit "))
# if n<100 :
#   print("No charge ")
# elif n<200:
#   print("Total charge :",(n-100)*5)
# elif n>200:
#   print("Total charge :",(n-100)*10)



# 9. Write a program to accept the cost price of a bike and display the road tax to be
# paid according to the following criteria :     
# Cost price (in Rs) Tax
# &gt; 100000 15 %
# &gt; 50000 and &lt;= 100000 10%
# &lt;= 50000 5%
# n=int(input("Enter cost price of the bike :"))
# if n>100000 :
#   print("Road tax to be paid is ",n*0.15)
# elif n>50000 and n<100000:
#   print("Road tax to be paid is ",n*0.1)
# elif n<50000:
#   print("Road tax to be paid is",n*0.05)


# 10. Accept the marked price from the user and  calculate the Net amount as(Marked
# Price –    Discount) to pay according to following criteria:
# mp=int(input("Enter market price :"))
# if mp>10000 :
#   print("Market price - discount=",mp*0.2)
# elif mp>7000 and mp<=10000:
#   print("Maret price -discount=",mp*0.15)
# elif mp<=70000:
#   print("Market price- discount=",mp*0.1)
