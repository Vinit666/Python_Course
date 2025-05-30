"""
reading a file by file handling

"""

# f = open(
#     "example.txt"
# )  # by default a file opens in read mode when you dont give any mode to open.


# # x = f.read()    #you can give in read () value that that will use as how many charcters would be read.
# y = f.read(10)  # it will read first 10 charcters.
# x = f.read(
#     10
# )  # now here it will read next 10 chareters from where it stop to read last time.
# print(y)
# print(x)

# f.close()


# f = open("example.txt")


# print(f.read())
# print(
#     f.read(100)
# )  # it will not read read anything because already the imagenery cursor at the end.

# f.close()


# f = open("example.txt")


# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.close()


# f = open("example.txt")


# print(
#     f.readlines()
# )  # it will read all lines and give output as a list where each index present each line.

# f.close()


# f = open("example.txt")

# print(f.readlines()[2])

# f.close()


# # by with keyword

# with open("example.txt") as f:
#     # print(f.read())
#     for line in f:
#         print(line)


# with open("example.txt") as f:
#     # print(f.read())
#     # for line in f:
#     #     print(line, end="")
#     x = f.read()
#     for ch in x:
#         print(ch)
