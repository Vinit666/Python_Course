"""Q39. Write a program that checks if a given year is a leap year. Leap years
are divisible by 4, but not by 100 unless they are also divisible by 400.
"""

y = int(input("Enter a year : "))

if y % 100 != 0 and y % 4 == 0 or y % 100 == 0 and y % 400 == 0:
    print("It is a Leep Year.")
else:
    print("It is a Aleep Year.")
