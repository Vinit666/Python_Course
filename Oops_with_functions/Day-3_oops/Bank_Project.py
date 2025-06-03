from random import randint


class bank:
    def __init__(self):
        print()
        self.name = input("Enter the name : ")
        self.acc_no = randint(100000, 200000)
        self.phone_no = input("Enter the Phone No. : ")
        self.current_bal = 0

    def deposit(self):
        deposit_amount = int(input("Enter the deposit amount : "))
        if deposit_amount >= 0:
            self.current_bal += deposit_amount
        else:
            print("Invalid, enter a valid amount.")

    def withdrawl(self):
        withdrawl_amount = int(input("Enter the withdrawl amount : "))

        if withdrawl_amount > self.current_bal:
            print("Insuficiant bank balance.")
        else:
            self.current_bal -= withdrawl_amount

    def check_balance(self):
        print(f"Current bank balance is : {self.current_bal}")

    def info(self):
        print(f"\nName of account holder is : {self.name}")
        print(f"Account No. is : {self.acc_no}")
        print(f"Current bank balance is : {self.current_bal}")
        print(f"Phone No. is : {self.phone_no}")


# a1 = bank()
# a1.deposit()
# a1.withdrawl()
# a1.info()
# a1.check_balance()
# print("-------------")
# print(a1.acc_no)


banks = []

while True:
    print("\n1.Create new Account.")
    print("2.Show all bank details.")
    print("3.deposit amount.")
    print("4.Withdrawl amount.")
    print("5.Exit.")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        obj = bank()
        banks.append(obj)

    elif choice == 2:
        print(banks)
        for obj in banks:
            obj.info()

    elif choice == 3:
        acc_num = int(input("For Deposit, Enter the Account no. : "))
        found = 0
        for obj in banks:
            if acc_num == obj.acc_no:
                obj.deposit()
                found += 1
        if found == 0:
            print("Account does not exist.")

    elif choice == 4:
        acc_num = int(input("For Withdrawl, Enter your Account no. : "))
        for obj in banks:
            if acc_num == obj.acc_no:
                obj.withdrawl()

    elif choice == 5:
        break

# l = [1, 2, 3, 4, 5, 6, 7]
# num = int(input("enter a num : "))
# for i in l:
#     if i == num:
#         print("yes in list")
#         break
# else:
#         print("not exist")
