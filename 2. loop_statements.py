# 1. Print multiplication table of a given number (1 x 1 = 1 …)
                                                 
# m=int(input("Enter a number :"))
# for n in range(1,11):
#   print(m,"*",n,"=",m*n)


# 2. Count the total number of digits in a number

# n = int(input("Enter a number :"))
# c = 0
# while n != 0:
#     n //= 10
#     c += 1
# print("Number of digits: " + str(c))



# 3. Print list in reverse order using a loop

# l1 = [10, 20, 30, 40, 50]
# c=len(l1)
# for i in range((c) -1,-1,-1):

#     print(l1[i], end=" ")



# 4. Print all prime numbers within a range

# start = int(input("Enter the start limit:"))
# end = int(input("Enter the end limit"))
# for num in range(start, end + 1):
#     if num > 1: # all prime #s are greater than 1
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)




# 5. Display Fibonacci series up to 10 terms

# n= int(input("Enter a number "))
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()



# 6. Reverse a integer number without using any built-in function

# n = int(input("Enter a number :"))
# r = 0
# while(n > 0):
#     a = n % 10
#     r= r * 10 + a
#     n = n // 10

# print(r)



# 8. Write a Python program that accepts a string and calculates the number of digits and letters. 
# Sample Data : Python 3.2
# Expected Output :
# Letters 6  Digits 2

# s = input("Input a string")
# a=0 # for alphabet
# d=0 # for digit
# for c in s:
#     if c.isdigit():
#         d = d + 1
#     elif c.isalpha():
#         a = a + 1
# print("Total alphabet:", a)
# print("Total Digits:", d)


# 9. Write a Python program to print the pattern using a  loop.
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# r = int(input("Enter number of rows:"))
# for i in range(0, r + 1):
#     for j in range(r - i, 0, -1):
#         print(j, end=' ')
#     print()


# b)
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# r = int(input("Enter the number of rows :"))
# for i in range(0, r):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(r, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")
                                                 