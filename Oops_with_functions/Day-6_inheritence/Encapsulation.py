# # three access modifiers --> Public , Private , Protected

# # Private mode--> it can be only call or used in same class also inherted class can't accesss it.
# from random import randint


# class Bank:
#     def __init__(self):
#         self.name = input("Enter your name : ")
#         self.account_no = randint(100000, 200000)
#         self.__bank_balance = int(
#             input("Enter your Bank balance : ")
#         )  # here you initialized bank balance in private mode by using __ before it.

#     def show_details(self):
#         print(f"Name is : {self.name}")
#         print(f"Account No. is : {self.account_no}")
#         print(f"Your Bank Balance is : {self.__bank_balance}")


# c1 = Bank()
# # c1.__bank_balance = 0 #it will not show any error but also not work to chenge the bank balance.
# # print(c1._Bank__bank_balance) # never use it but, by using this you can access that protected mode. but never use it.
# print("---------------")
# c1.show_details()


# protected mode--> in this a child class can access its parent class's protected mode but outside or globaly usally not in c++ but in python  you can also  access it and can change it.


class father:
    def __init__(self):
        self.f_name = "Vinit"
        self._bank_balance = 2000000000000  # here we initialized bank balance in protected mode by using _ before it.
        self.__phone_model = "Vivo Y73"

    def show_info(self):
        print(f"father name is : {self.f_name}")
        print(f"father Bank Balance is : {self._bank_balance}")
        print(f"father Phone Model is : {self.__phone_model}")


class child(father):
    def __init__(self):
        super().__init__()
        self.child_name = input("Enter Child Name : ")

    def show_child_info(self):
        print(f"Child Name is : {self.child_name}")
        print(f"Father Name is : {self.f_name}")
        print(f"Father Bank Balance is : {self._bank_balance}")
        # print(f"Father Phone model is : {self.__phone_model}")


c1 = child()
print()
c1.show_info()
print()
c1._bank_balance = 0
print()
c1.show_child_info()
