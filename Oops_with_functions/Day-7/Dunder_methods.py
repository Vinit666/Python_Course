from random import randint


# class bank:
#     def __init__(self):
#         self.name = input("Enter your name : ")
#         self.account_no = randint(1000000, 2000000)
#         self.b_balance = input("Enter your bank balance : ")

#     def __str__(self):  #it will override the pre written __str__() and call this ().when you print obj.
#         return "this is a Dunder method string."

#     def show_info(self):
#         print(f"Name is : {self.name}")
#         print(f"Account No. is : {self.account_no}")
#         print(f"Bank Balance is : {self.b_balance}")


# c1 = bank()
# c2 = bank()
# print()
# c1.show_info()
# print()
# print(c1)
# print(c2)


class bank:
    def __init__(self):
        self.name = input("Enter your name : ")
        self.account_no = randint(1000000, 2000000)
        self.b_balance = input("Enter your bank balance : ")

    def __str__(
        self,
    ):  # it will override the pre written __str__() and call this ().when you print obj.
        return f"Name is : {self.name}\nAccount No. is : {self.account_no}\nBank Balance is : {self.b_balance}"

    def show_info(self):
        print(f"Name is : {self.name}")
        print(f"Account No. is : {self.account_no}")
        print(f"Bank Balance is : {self.b_balance}")


c1 = bank()
c2 = bank()
print()
c1.show_info()
print()
print(c1)
print(c2)
