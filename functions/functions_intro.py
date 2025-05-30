# # how to define function--->

# # def function_name():
# #     lines of codes
# # function_name()


# # without parameters without return
# def sum():
#     print("hello world")
#     print("this is a good function.")


# sum()


# # with parametrs without return
# def sum_of(a, b):
#     print(a + b)


# sum_of(12, 3)


# def sum_of(a, b):
#     print(int(a) + int(b))


# # sum_of("a", "b")    #it will show error -->ValueError: invalid literal for int() with base 10: 'a'
# sum_of(12.2, 21.2)


# # with parametrs with return
# def greet(name):
#     g = print(f"hello {name}")
#     return g


# greet("vinit")
# print(type(greet))


# def sum(a, b):
#     return a + b


# def sum():
#     print("last wala")


# def sub(x, y):
#     print(x - y)


# # sum(1, 2)
# sum()
# # sub(10, sum(1, 2))


def sum():
    print("hello world")
    print("this is a good function.")


def sum(a, b):
    return a + b


def sum():
    print("last wala")


def sum(a, b):
    print(a + b)


sum(12, 2)
