"""Q131. Ask ‘n’ from user. Create a list of first n elements but in reverse order
using slicing."""

l = [1, 2, 3, 4, 5, 6, 7, 8, 90, 0]
print(f"list  is : {l}")
n = int(input("Enter the value of n : "))
print(f"first n elements but in reverse order is : {l[:n][::-1]}")
print(f"first n elements but in reverse order is : {l[n-1::-1]}")
