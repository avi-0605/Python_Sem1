
# #1 Write a Python program to compute the element-wise sum of given tuples. 
# n1 = input("Enter values for the 1st tuple (e.g., 1 2 3): ").split()
# n2 = input("Enter values for the 2nd tuple (e.g., 1 2 3): ").split()
# n3 = input("Enter values for the 3rd tuple (e.g., 1 2 3): ").split()
# t1 = tuple(map(int, n1))
# t2 = tuple(map(int, n2))
# t3 = tuple(map(int, n3))
# max_length = max(len(t1), len(t2), len(t3))
# result = []
# for i in range(max_length):
#   sum_value = (t1[i] if i < len(t1) else 0) + (t2[i] if i < len(t2) else 0) + (t3[i] if i < len(t3) else 0)
#   result.append(sum_value)
# print("Element-wise sum of the tuples:", result)



# #2 Write a Python program to convert a given list of tuples to a list of lists. 
# n = int(input("Enter the number of tuples: "))
# tuple_list = []
# for i in range(n):
#   tup = tuple(map(int, input(f"Enter values for tuple {i+1} (e.g., 1 2): ").split()))
#   tuple_list.append(tup)
#   list_of_lists = [list(tup) for tup in tuple_list]
# print("List of lists:", list_of_lists)




# #3 Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# tuple_list = [(1, 2), (2, 3), (3, 4)]
# list_of_lists = [list(tup) for tup in tuple_list]
# print("Converted list of tuples to a list of lists:", list_of_lists)


# #4 Write a Python program to remove an empty tuple(s) from a list of tuples
# tuple_list = [(), (1, 2), (), (3, 4), (5,)]
# non_empty_tuples = [t for t in tuple_list if t]
# print("List after removing empty tuples:", non_empty_tuples)


# #5 Write a Python program to convert a given string to a tuple
# input_string = input("Enter a string: ")
# string_tuple = tuple(input_string)
# print("Tuple from the string:", string_tuple)




# # 6 Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# def multiply_tuple(t):
#   product = 1
#   for num in t:
#     product *= num
#     return product
# tup = (2, 3, 5)
# result = multiply_tuple(tup)
# print("The product of the numbers in the tuple is:", result)