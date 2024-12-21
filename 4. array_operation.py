
# #1  Write a Python program to reverse the order of the items in the array.
# m= [1, 2, 3, 4, 5]
# r= m[::-1]
# print(r)

# #2  Write a Python program to get the number of occurrences of a specified element in an array.
# m = [1, 2, 3, 4, 5, 2, 2]
# e= int(input("Enter the element to count: "))
# count = m.count(e)
# print(f"The number of occurrences of {e} is: {count}")

# #3 Write a Python program to find out if a given array of integers contains any duplicate elements.

# m = [1, 2, 3, 4, 5, 6, 2]
# for i in m :
#     count = m.count(i)
# count = m.count(e)
# if count!=1:
#     print("Array contain duplicate element")
# else:
#   print("True")

# #4 Write a  Python program to find the missing number in a given array of 5 continuous numbers
# def f(arr):
#     expected_sum = sum(range(min(arr), max(arr) + 1))
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum

# array = [1, 2, 4, 5]
# missing_number = f(array)
# print("The missing number is:", missing_number)

# def r(arr):
#     return [-1 if x % 2 != 0 else x for x in arr]

# array = [1, 2, 3, 4, 5]
# m=r(array)
# print("Modified array:",m)