# #1 Python program to check whether the string is Symmetrical or Palindrome
# s=input("Enter a string:")
# if s==s[::-1]:
#   print("Print it is a palindrome")
# else:
#   print("Print it is not a palindrome")

# #2 Find length of a string in python without using len function
# l2=input("ENTER A STRING:")
# count=0
# print(l2.split())
# for i in l2 :
#   count+=1
# print(count)

# #3 Python Program to remove all duplicates from a given string
# s=input("Enter a string: ")
# n=""
# for c in s:
#   if c not in n:
#     n+=c

# print("String after removing duplicates:",n)

# #4 Maximum frequency character in String
# string =input("Enter a string : ")
# char_counts = {}
# for char in string:
#     char_counts[char] = char_counts.get(char, 0) + 1
# max_char = max(char_counts, key=char_counts.get)
# print("The maximum frequency character is:", max_char, "with frequency:", char_counts[max_char])

# #5 Write a Python program to count the number of characters in a string.
# s=input("Enter a string:")
# c={}
# for char in s:
#     c[char]=c.get(char, 0)+1
# print("Character counts:",c)

# #6 Count all letters, digits, and special symbols from a given string
# s=input("Enter a string :")
# l=0
# d=0
# sp=0
# for char in s:
#     if char.isalpha():
#         l+=1
#     elif char.isdigit():
#         d+=1
#     else:
#         sp+= 1
# print("Total number of ")
# print("Letters:",l)
# print("Digits:", d)
# print("Symbols:",sp)

# #7 Write a program which read incoming email, all emails not sent from the &quot;@itm.edu&quot; domain
# should be moved to the spam box.
# se=input("Enter sender email address: ")
# if "@itm.edu" not in se:
#     print("Moving email to spam box.")
# else:
#     print("Email is sent from @itm.edu domain.")

# #8 You are tasked to create a simple password validator. The validation rules are as follows:Password length of at least 8 characters.
# p=input("Enter the password :")
# if len(p)<8:
#   print("Password length should be at least 8 characters")
# for i in p:
#   if i.isupper():
#     print("Password should contain atleast one uppercase character")
#     break
#   elif i.islower():
#     print("Password should contain atleast one lowercase character")
#     break
#   elif i not in "!#$%&*+.?-~":
#     print("Password should contain atleast one special character")
#     break
# else:
#   print("Password is valid")