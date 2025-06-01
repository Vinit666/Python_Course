"""Q124. Generate a list of list using list comprehension where format should
be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]"""

l = [[i, "EVEN" if i % 2 == 0 else "ODD"] for i in range(1, 4)]
print(l)
