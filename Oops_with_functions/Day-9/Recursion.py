# Recursion--> when a function call itself then it will known as recursion.

# this code will raise error which is --->RecursionError: maximum recursion depth exceeded
# this will also raise a problem of stack overflow.
# def my_func():
#     print("this is a my func.")
#     my_func()


# my_func()


# this will manage the stackoverflow problem.
def my_func(num: int):
    print(f"this is a my func run time is :{num}.")
    if num == 1:
        return
    my_func(num - 1)


my_func(10)
