"""Q40. Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7.
"""

age = int(input("Enter the age : "))

if age < 12:
    print("Movie ticket cost is : $5")
elif age >= 12 and age <= 65:
    print("Movie ticket cost is : $10")
else:
    print("Movie ticket cost is : $7")
