# pickle-->

import pickle


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = student("vinit", 18)

# with open("example.txt", "w") as f:
#     # s = "hii my name is vinit"
#     f.write(str(s1))

# with open("example.txt", "r") as f:
#     s = f.read()
#     print(s)
#     print(type(s))

# pickle--->

# with open("example.txt", "wb") as f:
#     pickle.dump(s1, f)    #using this we can add or wirte an obj in a binary form in a file.


# with open("example.txt", "rb") as f:
#     s = f.read()
#     print(s)
#     print(type(s))


# unpickle:----> reading obj from file accesing the info of obj-->

with open("example.txt", "rb") as f:
    st_obj = pickle.load(
        f
    )  # using this we can load or read an obj and can use it for access the class atributes and methods.
    print(st_obj)
    print(type(st_obj))
    print(st_obj.name)
    print(st_obj.age)
