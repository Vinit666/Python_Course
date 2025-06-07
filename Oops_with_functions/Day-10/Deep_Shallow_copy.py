import copy

# a = [[12, 87, 98], [4, 90, 32], [32, 43, 556]]
# b = a

# print(a, id(a))
# print(b, id(b))
# print()
# a[0] = 100  #it will change in both a and b because a and b are one in memory.
# print(a)
# print(b)


# # shallow copy---> it is like copy but just outer copy inner parts still have same adderss if they are same.

# a = [[12, 87, 98], [4, 90, 32], [32, 43, 556]]
# b = copy.copy(a)

# print(a, id(a))
# print(b, id(b))  # now just outer parts of both a and b have different ids or memory locations.
# print()
# a[0] = 100  # it will change in only in a because a and b are shellow copy in memory.
# print(a)  # output-->[100, [4, 90, 32], [32, 43, 556]]
# print(b)  # output-->[[12, 87, 98], [4, 90, 32], [32, 43, 556]]


# Deep copy---> it is a copy not just outer copy but inner parts also have copy. it is a total differnt copy in deep .

a = [[12, 87, 98], [4, 90, 32], [32, 43, 556]]
b = copy.deepcopy(a)

print(a, id(a))
print(
    b, id(b)
)  # now both a and b have different ids or memory locations,with inner data also.
print()
a[0] = 100  # it will change in only in a ,because a and b are Deep copy in memory.
a[1][0] = 100  # it will change in only in a ,because a and b are Deep copy in memory.
print(a)  # output-->[100, [4, 90, 32], [32, 43, 556]]
print(b)  # output-->[[12, 87, 98], [4, 90, 32], [32, 43, 556]]
