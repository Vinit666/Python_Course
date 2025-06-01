"""Q128. Implement a python program to get the last 'n' elements from a list
using slicing.
"""

l = [1, 2, 3, 4, "vinit", "hii", "hello", "you", 6, 7, 8, 9, 0]
print(f"List is : {l}")
n = int(input("Enter the value for get the last n elements : "))
print(f"last {n} elements from list is : {l[-n:]}")
