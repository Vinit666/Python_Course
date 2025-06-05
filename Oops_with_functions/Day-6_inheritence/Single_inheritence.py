# class car:
#     def set_base_info(
#         self, color: str, type: str, mileage: float, seat_capacity: int
#     ) -> None:
#         self.color = color
#         self.type = type
#         self.mileage = mileage
#         self.seat_capacity = seat_capacity

#     def base_info(self) -> print:
#         print(f"Color is : {self.color}")
#         print(f"Type is : {self.type}")
#         print(f"Mileage is : {self.mileage}")
#         print(f"Seat Capacity is : {self.seat_capacity}")


# class audi(
#     car
# ):  # here we, in audi class car class inherted.and this is a single inhertence means single class is inheted by another single class.
#     def set_audi_info(self, electric: bool, city: str) -> None:
#         self.electric = electric
#         self.city = city

#     def audi_info(self):
#         print(f"Electric : {self.electric}")
#         print(f"City is : {self.city}")

#     def show_full_info(self):
#         self.base_info()
#         self.audi_info()


# c1 = audi()
# c1.color = "Black"
# c1.type = "Petrol"
# c1.mileage = 22.2
# c1.seat_capacity = 5
# c1.electric = "Yes"
# c1.city = "Sikar"
# c1.base_info()
# print("-----------------")
# c1.audi_info()
# print("-----------------")
# c1.show_full_info()


"""classes without parameters and takes input from user."""


# class car:
#     def set_base_info(self) -> None:
#         self.color = input("Enter the Color of car : ")
#         self.type = input("Enter the Type of car : ")
#         self.mileage = float(input("Enter the Mileage of car : "))
#         self.seat_capacity = int(input("Enter the Seat Capacity of car : "))

#     def base_info(self) -> print:
#         print(f"Color is : {self.color}")
#         print(f"Type is : {self.type}")
#         print(f"Mileage is : {self.mileage}")
#         print(f"Seat Capacity is : {self.seat_capacity}")


# class audi(
#     car
# ):  # here we, in audi class car class inherted.and this is a single inhertence means single class is inheted by another single class.
#     def set_audi_info(self) -> None:
#         self.electric = input("Enter the Electric Status of car : ")
#         self.city = input("Enter the City of car : ")

#     def audi_info(self):
#         print(f"Electric status : {self.electric}")
#         print(f"City is : {self.city}")

#     def show_full_info(self):
#         self.base_info()
#         self.audi_info()


# c1 = audi()
# c1.set_base_info()
# c1.set_audi_info()
# print("-----------------")
# c1.base_info()
# print("-----------------")
# c1.audi_info()
# print("-----------------")
# c1.show_full_info()


""" Methods to short the code like using __init__ () ---> only one init () using in child class(audi class)"""


# class car:
#     def set_base_info(self) -> None:
#         self.color = input("Enter the Color of car : ")
#         self.type = input("Enter the Type of car : ")
#         self.mileage = float(input("Enter the Mileage of car : "))
#         self.seat_capacity = int(input("Enter the Seat Capacity of car : "))

#     def base_info(self) -> print:
#         print(f"Color is : {self.color}")
#         print(f"Type is : {self.type}")
#         print(f"Mileage is : {self.mileage}")
#         print(f"Seat Capacity is : {self.seat_capacity}")


# class audi(
#     car
# ):  # here we, in audi class car class inherted.and this is a single inhertence means single class is inheted by another single class.
#     def __init__(self) -> None:
#         self.set_base_info()
#         self.electric = input("Enter the Electric Status of car : ")
#         self.city = input("Enter the City of car : ")

#     def audi_info(self):
#         print(f"Electric status : {self.electric}")
#         print(f"City is : {self.city}")

#     def show_full_info(self):
#         self.base_info()
#         self.audi_info()


# c1 = audi()
# print("-----------------")
# c1.base_info()
# print("-----------------")
# c1.audi_info()
# print("-----------------")
# c1.show_full_info()


""" Methods to short the code like using __init__ () ---> using 2 init()  in both child class(audi class) and parent class(car class)"""


class car:
    def __init__(self) -> None:
        self.color = input("Enter the Color of car : ")
        self.type = input("Enter the Type of car : ")
        self.mileage = float(input("Enter the Mileage of car : "))
        self.seat_capacity = int(input("Enter the Seat Capacity of car : "))

    def base_info(self) -> print:
        print(f"Color is : {self.color}")
        print(f"Type is : {self.type}")
        print(f"Mileage is : {self.mileage}")
        print(f"Seat Capacity is : {self.seat_capacity}")


class audi(
    car
):  # here we, in audi class car class inherted.and this is a single inhertence means single class is inheted by another single class.
    def __init__(self) -> None:
        super().__init__()  # if we want to call the init() of the base class then we use super() to call it.
        self.electric = input("Enter the Electric Status of car : ")
        self.city = input("Enter the City of car : ")

    def audi_info(self):
        print(f"Electric status : {self.electric}")
        print(f"City is : {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()


c1 = audi()
print("-----------------")
c1.base_info()
print("-----------------")
c1.audi_info()
print("-----------------")
c1.show_full_info()
