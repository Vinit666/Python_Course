"""Q122. Given a list of strings, create a new list containing the lengths of
each string using list comprehension.
"""

l = ["dffev", "ewf", "rvervqerv", "5+ce48", "vinit", "kumawat"]
print(f"original list is : {l}")

l1 = [len(i) for i in l]
print(f"the lenght of the strings in list l is : {l1}")
