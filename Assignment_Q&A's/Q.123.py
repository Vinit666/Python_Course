"""Q123. Generate a list of strings where each string repeats itself three times,
using list comprehension.
"""

l = ["vinit", "hii", "kumawat", "bye"]
print(l)
l1 = [i * 3 for i in l]
print(l1)
l2 = [i for i in l for j in range(0, 3)]
print(l2)
