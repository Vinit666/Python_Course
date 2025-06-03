"""
class-->it is like a blue print.where all the methods and ojects are defined and contained.
objects---> objects are like an accessing a class and there can be any numbers of objects for a same class.

"""

# class student:
#     # class attributes
#     id = 0
#     name = " "
#     roll_no = 0
#     gender = " "

#     # class methods ---> in a class defining a function is known as a class method
#     def get_info(self):
#         print(f"Student ID is : {self.id}")
#         print(f"Student Name is : {self.name}")
#         print(f"Student Roll No. is : {self.roll_no}")
#         print(f"Student Gender is : {self.gender}")

#     def set_info(self):
#         self.id = int(input("Enter the ID of student : "))
#         self.name = input("Enter the Name of student : ")
#         self.roll_no = int(input("Enter the Roll No. of student : "))
#         self.gender = input("Enter the Gender of student : ")


# s1 = student()
# s1.set_info()
# s1.get_info()

# s2 = student()
# s2.set_info()
# s2.get_info()

# print(s1.roll_no)


# # METHOD ---->1

# class Student:
#     # these are class object
#     name = " "
#     id = 0
#     roll_no = 0
#     gender = " "


# s1 = Student()
# s1.name = "vinit"
# s1.id = 1
# s1.roll_no = 101
# s1.gender = "male"

# print(s1.name, end=" ")
# print(s1.id, end=" ")
# print(s1.roll_no, end=" ")
# print(s1.gender, end=" ")


# # METHOD ---->2


# class Student:
#     name = " "
#     id = 0
#     roll_no = 0
#     gender = " "

#     # class methods :--> these function in class called mehtod
#     def info(self):
#         print(f"Student name is : {self.name} ")
#         print(f"Student id is : {self.id} ")
#         print(f"Student roll_no  is : {self.roll_no}")
#         print(f"Student gender is : {self.gender} ")
#         print("\n")

#     def set_info(self):
#         self.name = input("Enter student name : ")
#         self.id = input("Enter student id : ")
#         self.roll_no = input("Enter student roll_no : ")
#         self.gender = input("Enter student gender : ")
#         print("\n")


# s1 = Student()
# s2 = Student()
# s1.set_info()
# s2.set_info()
# s1.info()
# s2.info()


# # METHOD ---->3


# class Student:
#     def info(self):
#         print(f"Student name is : {self.name} ")
#         print(f"Student id is : {self.id} ")
#         print(f"Student roll_no  is : {self.roll_no}")
#         print(f"Student gender is : {self.gender} ")
#         print("\n")

#     def set_info(self):
#         self.name = input("Enter student name : ")
#         self.id = input("Enter student id : ")
#         self.roll_no = input("Enter student roll_no : ")
#         self.gender = input("Enter student gender : ")
#         print("\n")


# s1 = Student()
# s2 = Student()
# # we first use set_info method  bez of make attributes/varibles
# s1.set_info()
# s2.set_info()
# # we cannot use info method before set_info
# s1.info()
# s2.info()


# METHOD ---->4
# using __init__()--->when a class object of class is created then it will call by default init() so we can set the values by init function.


class Student:
    def _init_(self):
        self.name = input("Enter student name : ")
        self.id = input("Enter student id : ")
        self.roll_no = input("Enter student roll_no : ")
        self.gender = input("Enter student gender : ")
        print("\n")

    def info(self):
        print(f"Student name is : {self.name} ")
        print(f"Student id is : {self.id} ")
        print(f"Student roll_no  is : {self.roll_no}")
        print(f"Student gender is : {self.gender} ")
        print("\n")


s1 = Student()  # when we create object then automatically access the init method
s2 = Student()
# we cannot use info method before set_info
s1.info()
s2.info()
