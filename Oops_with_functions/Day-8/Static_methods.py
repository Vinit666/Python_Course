from datetime import datetime


# class calender:
#     def __init__(self):
#         self.events = []

#     def add_event(self, e_name: str) -> None:
#         self.events.append(e_name)

#     def show_events(self):
#         print(f"Events are : {self.events}")

#     @staticmethod
#     def is_weekend(date: datetime):
#         if date.weekday() > 4:
#             print("It is a weekend.")

#         else:
#             print("It is a weekday.")
#             print(f"day is : {date}")


# c1 = calender()
# c1.add_event("dsa")
# c1.add_event("party")
# c1.add_event("coding")
# c1.show_events()
# c1.is_weekend(date=datetime.now())
# print()
# new_date = datetime.today()
# c1.is_weekend(date=new_date)


# staic outside the class-->
@staticmethod
def is_weekend(date: datetime):
    if date.weekday() > 4:
        print("It is a weekend.")  # weekend=Saturady,sunday

    else:
        print("It is a weekday.")
        print(f"day is : {date}")


class calender:
    def __init__(self):
        self.events = []

    def add_event(self, e_name: str) -> None:
        self.events.append(e_name)

    def show_events(self):
        print(f"Events are : {self.events}")


c1 = calender()
c1.add_event("dsa")
c1.add_event("party")
c1.add_event("coding")
c1.show_events()
is_weekend(date=datetime.now())
print()
new_date = datetime.today()
is_weekend(date=new_date)
