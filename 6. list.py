

# #1 Write a Python program to remove duplicates from a list.

# def newlist(oldlist):
#   new_list = []
#   for item in oldlist:
#     if item not in new_list:
#       new_list.append(item)
#   return new_list
# my_list = list(input("Enter elements to be in a list :"))
# unique_list = newlist(my_list)
# print("Original list:", my_list)
# print("List after removing duplicates:", unique_list)



# #2 Write a Python function that takes two lists and returns True if they have at least one common member.
# def common(list1, list2):

#   for i1 in list1:
#     if i1 in list2:
#       return True
#   return False
# list1 = list(input("enter elemts in list one :"))
# list2 = list(input("enter elemts in list two :"))
# print(list1)
# print(list2)
# if common(list1, list2):
#   print("The lists have at least one common member.")
# else:
#   print("The lists do not have any common members.")




# #3Write a Python program to print the numbers of a specified list after removing even numbers from it.
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers=[]

# for number in numbers:
#   if number % 2 != 0:
#     odd_numbers.append(number)

# print("List after removing even numbers:",odd_numbers)




# #4 Write a Python program to find the second smallest number in a list.
# inpu=input("Enter the number to temm second smallest value: ").split(" ")
# inpu=[int(i) for i in inpu]

# # Check if the list has at least two elements before proceeding
# if len(inpu) < 2:
#     print("Please enter at least two numbers to find the second smallest.")
# else:
#     # Remove the smallest element
#     inpu.remove(min(inpu))
#     # Print the second smallest (which is now the smallest after removal)
#     print(f"The second smallest value is {min(inpu)} ")




# #7 Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
# def is_palindrome_list(input_list):
#   return input_list == input_list[::-1]

# i=input("Enter a list of elements separated by spaces: ")
# e=i.split()
# list_elements = [int(element) for element in e]
# if is_palindrome_list(list_elements):
#   print("The list is a palindrome.")
# else:
#   print("The list is not a palindrome.")