from datetime import datetime

from time import sleep


# #printing new methods-->
# a = "vinit"
# b = 900

# print("a is %s and b is %d" % (a, b))  # output--->a is vinit and b is 900
# print("a is {} and b is {}".format(a, b))  # output--->a is vinit and b is 900


# # doc reading of a func--->
# def sum_of():
#     """hii this is a comment doc of a function."""
#     print("hii func runs successfully.")


# print(sum_of.__doc__)
# print(print.__doc__)


# def cal_time(func):
#     def wrapper(*args):
#         print("start decorator")
#         func(*args)
#         print("end decorator")

#     return wrapper


# @cal_time
# def sum_of(*args):
#     print(f"sum of a, b : {sum(args)}")


# sum_of(1, 2, 34, 4)

"""
output--->
start decorator
sum of a, b : 41
end decorator

"""


def cal_time(func):
    def wrapper(*args):
        print("start decorator")
        start_time = datetime.now()
        sleep(1)
        func(*args)
        end_time = datetime.now()
        print(f"total time : {end_time-start_time}")
        print("end decorator")

    return wrapper


@cal_time
def sum_of(*args):
    print(f"sum of a, b : {sum(args)}")


sum_of(1, 2, 34, 4)


""" 
output--->
start decorator
sum of a, b : 41
total time : 0:00:01.001367
end decorator

"""
