# class student:
#     def __init__(self, name: str, age: int, gender: str) -> None:
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def show_student(self):
#         print(f"student name is : {self.name}")
#         print(f"student age is : {self.age}")
#         print(f"student gender is : {self.gender}")


# s1 = student("Vinit", 21, "male")
# s1.show_student()


"""using class method with parameters"""


# class student:
#     def __init__(self, name: str, age: int, gender: str) -> None:
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def show_student(self):
#         print(f"student name is : {self.name}")
#         print(f"student age is : {self.age}")
#         print(f"student gender is : {self.gender}")

#     @classmethod
#     def create_student_using_params(cls, name, age, gender):
#         obj = cls(name, age, gender)
#         return obj


# s1 = student.create_student_using_params("Vinit", 21, "male")
# s1.show_student()


""" using class method with file """


class student:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def show_student(self):
        print(f"student name is : {self.name}")
        print(f"student age is : {self.age}")
        print(f"student gender is : {self.gender}")

    @classmethod
    def create_student_using_file(cls, file_name):
        f = open(file_name, "r")
        student_data = f.read()
        name, age, gender = student_data.split()
        f.close()

        obj = cls(name, age, gender)
        return obj


s1 = student.create_student_using_file("student.txt")
s1.show_student()
