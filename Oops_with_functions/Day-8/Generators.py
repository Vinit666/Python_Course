# yield is a generator--> it gives values 1 by 1.


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


x = numbers()
print(x)  # output--><generator object numbers at 0x000001FD675F5A60>
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))  #here it will give error of StopIteration.


for i in numbers():
    print(i)


# how to raise error by yourself

raise ZeroDivisionError  # error raised by raise
