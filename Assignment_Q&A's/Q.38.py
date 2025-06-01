"""Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are different.
"""

n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))

if n1 == n2 or n2 == n3 or n3 == n1 or n1 == n2 == n3:
    print("All or any two numbers are same, Try with all different numbers.")
elif n1 > n2 > n3:
    print(f"1st number {n1} is largest.")
elif n1 < n2 > n3:
    print(f"2nd number {n2} is largest.")
else:
    print(f"3rd number {n3} is largest.")
