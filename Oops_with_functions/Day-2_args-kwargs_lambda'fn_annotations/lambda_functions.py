"""lambda functions are anonymous functions.
because the are anonymous fun.,they cant be call by name so well call them by defining in a variable.
"""

# print_num = lambda num: print(num)

# print_num(12)  # output-->12


# sum_of = lambda *args: print(sum(args))

# sum_of(1, 2, 3, 4, 4)


# check_even = lambda num: num % 2 == 0

# print(check_even(1))  # output--->False
# print(check_even(12))  # output--->True

# if check_even(12):  # output--->Even
#     print("Even")
# else:
#     print("Odd")

# if check_even(1):  # output--->Odd
#     print("Even")
# else:
#     print("Odd")

# check_even = lambda num: print("Even") if num % 2 == 0 else print("Odd")

# check_even(23)  # output-->Odd
# check_even(2)  # output-->Even


make_list = lambda num: [i for i in range(0, num + 1)]
num1 = int(input("Enter a num : "))

print(make_list(num1))
