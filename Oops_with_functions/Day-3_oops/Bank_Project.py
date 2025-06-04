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
    print("5.For money transction.")
    print("6.Exit.")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        obj = bank()
        banks.append(obj)

    elif choice == 2:
        if len(banks) == 0:
            print("There is no account found.\nFirst, create a account.")
        else:
            for obj in banks:
                obj.info()

    elif choice == 3:
        if len(banks) == 0:
            print("There is no account found.\nFirst, create a account.")
        else:
            acc_num = int(input("For Deposit, Enter the Account no. : "))
            found = 0
            for obj in banks:
                if acc_num == obj.acc_no:
                    obj.deposit()
                    found += 1
            if found == 0:
                print("Account does not exist.")

    elif choice == 4:
        if len(banks) == 0:
            print("There is no account found.\nFirst, create a account.")
        else:
            acc_num = int(input("For Withdrawl, Enter your Account no. : "))
            found = 0
            for obj in banks:
                if acc_num == obj.acc_no:
                    obj.withdrawl()
                    found += 1
            if found == 0:
                print("Account does not exist.")
    elif choice == 5:
        if len(banks) == 0:
            print("There is no account found.\nFirst, create a account.")
        else:
            Sender_acc_num = int(
                input("For Transction, Enter Sender's(Your) Account no. : ")
            )
            Sender_found = 0
            for Sender_obj in banks:
                if Sender_acc_num == Sender_obj.acc_no:
                    Receiver_acc_num = int(
                        input("For Transction, Enter Receiver's Account no. : ")
                    )
                    Receiver_found = 0
                    for Receiver_obj in banks:
                        if Receiver_acc_num == Receiver_obj.acc_no:
                            Receiver_found += 1
                            transfer_amount = int(
                                input("For Transfer, Enter the amount : ")
                            )
                            if transfer_amount <= Sender_obj.current_bal:
                                Sender_obj.current_bal -= transfer_amount
                                Receiver_obj.current_bal += transfer_amount
                            else:
                                print("Insuficient bank balance.")

                    if Receiver_found == 0:
                        print("Receiver's Account does not exist.")
                    Sender_found += 1

            if Sender_found == 0:
                print("Sender's Account does not exist.")

    elif choice == 6:
        break

# l = [1, 2, 3, 4, 5, 6, 7]
# num = int(input("enter a num : "))
# for i in l:
#     if i == num:
#         print("yes in list")
#         break
# else:
#         print("not exist")
