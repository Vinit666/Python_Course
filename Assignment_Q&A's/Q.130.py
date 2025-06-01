"""Q.130.Ask start and end index from the user. Create a list from start index
to end index using slicing.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"list is : {l}")
s = int(input("Enter the start index : "))
e = int(input("Enter the end index : "))
print(f"new list from {s} to {e} is : {l[s:e]}")
