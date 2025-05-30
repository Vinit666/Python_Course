"""
try:
    lines of code

    if any error then it will print except block

except:
    print("some error occured.")

"""

try:
    my_list = [1, 2, 3, 4, 5, 45, 90, 54]
    print(my_list[0])
    print(
        my_list[12]
    )  # from here error occured and from her it will throw to excep block to execution.
    print(my_list[2])
    print(my_list[4])
except:
    print("!!!Some error occured!!!")
print("ok done")
print("bye")

# output--->    1
#               !!!Some error occured!!!
#               ok done
#               bye


try:
    my_list = [1, 2, 3, 4, 5, 45, 90, 54]
    print(my_list[0])
    print(
        my_list[12]
    )  # from here error occured and from her it will throw to excep block to execution.
    print(my_list[2])
    print(my_list[4])
except IndexError:
    print("! Invalid index !")
except ZeroDivisionError:
    print("! you can not divide by zero !")
except:
    print("!!!Some error occured!!!")
else:
    print(
        "Everything worked fine."
    )  # this will run when all try block runs successfully.
finally:
    print(
        "This is Finally clause."
    )  # this will run definately as a finally clause.when there is any error occured or not.
print("ok done")
print("bye")
