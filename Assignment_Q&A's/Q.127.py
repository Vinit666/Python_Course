"""Q127. Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17]
print(f"original list is : {l}")

l1 = l[: (len(l) // 2)]
print(f"half list is : {l1}")
l2 = l[(len(l) // 2) : :]
print(f"remaining half list is : {l2}")
