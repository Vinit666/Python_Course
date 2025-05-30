"""
Q166. Write a function that accepts an integer and prints the
multiplication table for that number up to 10.

"""

# def table(n):
#     print(f"Table of {n} is : ")
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")


# # call by value
# table(8)

# # call by reference
# a = 7
# table(a)


# --------------------------------------------------------------------------------------------------------------------------------

"""
Q167. Write a function that accepts an integer and prints whether it is odd
or even.

"""


# def check(n):
#     if n == 0:
#         print(f"{n} is not an even and an odd number.")
#     elif int(n) % 2 == 0:
#         print(f"{n} is even number.")
#     else:
#         print(f"{n} is odd number.")


# check(9872)
# --------------------------------------------------------------------------------------------------------------------------------

"""
Q168. Write a function that takes three numbers as parameters and prints
the largest among them.

"""


# def largest(a, b, c):
#     if a >= b >= c:
#         print(f"{a} is the largest.")
#     elif a < b >= c:
#         print(f"{b} is the largest.")
#     else:
#         print(f"{c} is the largest.")


# largest(56, 4, 234)


# --------------------------------------------------------------------------------------------------------------------------------
"""
Q169. Write a function that takes an integer and prints whether it is a prime number.

"""


# def is_prime(a):
#     c = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             c += 1
#     if c == 2:
#         print(f"{a} is a prime number.")
#     else:
#         print(f"{a} is not a prime number.")


# is_prime(11)


# --------------------------------------------------------------------------------------------------------------------------------

"""
Q170. Write a function that takes a list of numbers and prints the sum and
average of these numbers.

"""


# def list_sum_and_avg(a=[]):
#     s = 0
#     for i in a:
#         s += i
#     print(f"sum of list is : {s}")
#     print(f"average of list is :{s/len(a)}")


# list_sum_and_avg(a=[1, 2, 3.5, 4, 5])


# --------------------------------------------------------------------------------------------------------------------------------

"""
Q171. Write a function that accepts a string and prints the frequency of
each character in the string.

"""


# def f_of_string(s=""):
#     d = {}
#     for i in s:
#         d[i] = s.count(i)
#     for k, v in d.items():
#         print(f"frequency of {k} is {v}")


# f_of_string(s="vinit vinit vin")

# --------------------------------------------------------------------------------------------------------------------------------

"""
Q172. Write a function that takes a string and prints whether it is a
palindrome.
"""


# def is_palindrome(a=""):
#     if a == a[::-1]:
#         print(f"it is a palindrome.")
#     else:
#         print(f"It is not a palindrome.")


# is_palindrome("vinit")
