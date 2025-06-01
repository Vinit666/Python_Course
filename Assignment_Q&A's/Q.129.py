"""Q.129.Ask ‘n’ from user. Create a list of last n elements but in reverse order
using slicing"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"list is : {l}")
n = int(input("Enter the value of n : "))
# method 1
print(f"last n elements list in reverse order is : {l[:-n-1:-1]}")
# method 2
print(f"last n elements list in reverse order is : {l[-n:][::-1]}")
