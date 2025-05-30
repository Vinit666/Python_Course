# # how to open a file in write mode or if the file  not exist then it will be created automatically.
# with open("index1.txt", "w") as f:
#     print(f.write("hello world"))

# with open("index1.txt", "a") as f:
#     f.write("\nVinit kumawat")

# with open("index1.txt", "a") as f:
#     f.write("\ndinesh kumawat")


# file = input("Enter file name (withoout extension) : ")
# f_name = file + ".txt"


# with open(f_name, "a") as f:
#     f.write("good ho tum")

# with open("new.txt", "w") as f:
#     f.write("hello world")
#     f.write("\nbye")


file = input("Enter file name (withoout extension) : ")
f_name = file + ".txt"


with open(f_name, "w") as f:
    while True:
        line = input("Enter the line data : ")
        if line == "q" or line == "Q":
            break
        else:
            f.write(f"\n{line}")
