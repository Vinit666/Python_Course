"""
Q1. Write a Python function to reverse a string using slicing and return it.

"""

# def s_reverse(s=""):
#     return s[::-1]


# s_reverse("vinit")
# print(s_reverse("vinit"))


# -------------------------------------------------------------------------------------------------------------------------------
"""
Q2. Write a Python function that accepts a string and counts the number of upper and lower case letters. 1

"""


# def s_ul_count(s=""):
#     cu = 0
#     cl = 0
#     for i in s:
#         if i.isalpha():
#             if i.isupper():
#                 cu += 1
#             else:
#                 cl += 1
#     print(f"upper count is : {cu}")
#     print(f"lower count is : {cl}")


# s_ul_count("v78iN^iT#$")

# -------------------------------------------------------------------------------------------------------------------------------

"""
Q3. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

Sample List: [10,20,20,20,10,10,50]

Unique List: [10,20,50]

"""

# #method -1
# def list_distinct(l=[]):
#     ul = []
#     for i in l:
#         if i not in ul:
#             ul.append(i)
#     print(f"distinct list is : {ul}")


# list_distinct([1, 2, 3, 1, 2, 3, 1, 6, 7, "vinit"])


# # method-2
# def list_dist(l=[]):
#     s = set(l)
#     nl = list(s)
#     print(f"distinct list is : {nl}")


# list_dist([1, 2, 3, 1, 2, 3, 20, "vinit"])


# -------------------------------------------------------------------------------------------------------------------------------

"""
Q4. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

"""


# def is_prime(num):
#     c = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             c += 1
#     if c == 2:
#         print(f"{num} is prime.")
#     else:
#         print(f"{num} is not a prime.")


# is_prime(41)
# -------------------------------------------------------------------------------------------------------------------------------

"""
Q5. Write a Python function that takes start_number and end_number as a parameter. Now print all the prime numbers between start_number to end_number.

"""


# def print_prime(start_number=0, end_number=0):
#     l = []
#     for i in range(start_number, end_number + 1):
#         c = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 c += 1
#         if c == 2:
#             l.append(i)
#     print(f"prime numbers from {start_number} to {end_number} is : {l}")


# print_prime(1, 200)


# -------------------------------------------------------------------------------------------------------------------------------

"""
Q6. Python function to print even length words in a string.

"""


def count_even_lenght_word__in_string(s=""):
    l = s.split()
    nl = []
    for i in l:
        c = 0
        for j in i:
            c += 1
        if c % 2 == 0:
            nl.append(i)
    print(f"Even length words in a string are : {nl}")


count_even_lenght_word__in_string("hii my name is vinit kuma and what is your     name")
