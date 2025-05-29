"""
Q158. Given two lists a, b. Check if two lists have at least one element common in them.

"""

a = [1, 2, 3, 4, 5, 54, 7, 76, 5, 8, 98, 7]
b = [1, 32, 43, 43, 54, 5, 45, 3, 2, 32, 2, 12, 12]

a = [1, 2, 3, 4, 5]
b = [5, 6, 9, 7, 8, 1]

print(f"a = {a}")
print(f"b = {b}")

set1 = set(a)
set2 = set(b)
c = list(set1.intersection(set2))

if len(c) == 0:
    print("No common elements in the both lists.")
else:
    print(f"both lists have {len(c)} common elements.")
    print(f"Common elements in both lists are : {c}")


# -------------------------------------------------------------------------------------------------------------------------------

"""
Q159. Python program to find common elements in three lists using sets.

"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 3, 5, 7, 9, 11]
c = [2, 4, 6, 1, 7, 5, 12, 11, 8]

print(f"list a = {a}")
print(f"list b = {b}")
print(f"list c = {c}")

s1 = set(a)
s2 = set(b)
s3 = set(c)

c = list(s1.intersection(s2.intersection(s3)))

if len(c) == 0:
    print("No common elements in the both lists.")
else:
    print(f"both lists have {len(c)} common elements.")
    print(f"Common elements in both lists are : {c}")


# -------------------------------------------------------------------------------------------------------------------------------


"""
Q160. Create 3 sets of your own, find the union of three sets.

"""
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {1, 3, 5, 7, 9, 11}
c = {2, 4, 6, 1, 7, 5, 12, 11, 8}

print(f"set 1 is : {a}")
print(f"set 2 is : {b}")
print(f"set 3 is : {c}")

print(f"\nUnion of the all 3 sets is : {a.union(b.union(c))}")

# -------------------------------------------------------------------------------------------------------------------------------


"""
Q161. Write a Python program to remove all elements from a given set.

"""
a = {1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8}
print(f"set is : {a}")

for i in range(0, len(a)):
    a.pop()
print(f"After removing the all values from the set : {a}")

# -------------------------------------------------------------------------------------------------------------------------------


"""
Q162. Write a Python program to find the length of a set.

"""
a = {1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8}
print(f"set is : {a}")

# method - 1
print(f"lenght of set is : {len(a)}")

# method - 2
c = 0
for i in a:
    c += 1
print(f"lenght of set is : {c}")


# -------------------------------------------------------------------------------------------------------------------------------


"""
Q163. Write a Python program to check if two given sets have no elements in common.

"""
a = {1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8}
b = {12, 23, 34, 45, 56, 67, 78, 89, 90, 123, 345, 432, 321, 111, 222}
print(f"set a is : {a}")
print(f"set b is : {b}")

c = set(a.intersection(b))

if len(c) == 0:  # method -2 --->if c=set{}:
    print("both sets have no common elements.")
else:
    print(f"both sets have {len(c)} common elements that are : {c}")


# -------------------------------------------------------------------------------------------------------------------------------


"""
Q164. Write a Python program to find elements in a given set that are not in another set.

"""
a = {1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8}
b = {12, 23, 3, 2, 34, 45, 56, 67, 78, 89, 90, 123, 345, 432, 321, 111, 222, 8}
print(f"set a is : {a}")
print(f"set b is : {b}")

iab = list(a.intersection(b))

nc = a.copy()
for i in iab:
    nc.remove(i)
print(f"elements in set a that are not in set b is : {nc}")


# -------------------------------------------------------------------------------------------------------------------------------


"""
Q165. Ask a string from user, remove all the duplicates from that string and print that string again (order does'nt matter)

"""

s = input("Enter a string : ")
s1 = set(s)

ns = str()
for i in s1:
    ns += i
print(f"After removing all deblictes from string then new string is : {ns}")
