class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("Destructor called.")
        del self.gender


s1 = student("Vinit", 21, "Male")
print(s1.name)
print(s1.age)
print(s1.gender)
# s1.__del__()
# print(s1.gender)
