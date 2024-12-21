# #1 Write a Python function to check whether a number falls within a given range.
# def check(number, start, end):
#   return start <= number <= end

# s=int(input("Enter the start of the range: "))
# e=int(input("Enter the end of the range: "))
# n=int(input("Enter a number: "))

# if check(n,s,e):
#   print(f"{n} is within the range (", s, ",", e, ")")
# else:
#   print(f"{n} is not within the range (", s, ",", e, ")")

# #2 Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list
# def find(words):
#   if not words:
#     return None, None

#   shortword = words[0]
#   longword = words[0]

#   for word in words:
#     if len(word)<len(shortword):
#       shortest_word = word
#     if len(word)>len(longword):
#       longword=word

#   return shortword,longword
# words = ["apple", "banana", "cherry", "date", "blueberry"]
# shortest,longest=find(words)
# print("Shortest word:", shortest)
# print("Longest word:", longest)

# #3 Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.
# def add(inlist,e):
#   if e not in inlist:
#     inlist.append(e)
#   return inlist

# my_list = []
# while True:
#   e= input("Enter an element to add or type 'exit' to stop): ")
#   if e.lower()=='exit':
#     break
#   my_list = add(my_list,e)
#   print("Updated list:", my_list)

# #4 Write a program to implement these formulae of permutations and combinations
# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n*factorial(n-1)

# def permutations(n,r):
#   return factorial(n)//factorial(n-r)

# def combinations(n,r):
#   return factorial(n)//(factorial(r)*factorial(n-r))

# n=int(input("Enter the value of n: "))
# r=int(input("Enter the value of r: "))

# print("Number of permutations:",permutations(n,r))
# print("Number of combinations:",combinations(n,r))

# #5 A number is called perfect if the sum of proper divisors of that number is equal to the number.
# def perfect(n):
#   sum=0
#   for i in range(1, n):
#     if n%i==0:
#       sum+=i
#   return sum==n

# def perfectnum(start, end):
#   for i in range(start, end + 1):
#     if perfect(i):
#       print(i)

# start=int(input("Enter the start of the range: "))
# end=int(input("Enter the end of the range: "))

# perfectnum(start, end)

# #6 Write a recursive function that will return the nth term of the Fibonacci sequence.
# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("Enter a value : "))
# if n < 0:
#   print("Incorrect input")
# else:
#   print(f"The",n,"th Fibonacci number is:", fibonacci(n))