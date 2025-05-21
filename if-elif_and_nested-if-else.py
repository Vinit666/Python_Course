
"""  Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero
"""
# num=int(input("Enter a Number : "))
# if num==0:
#     print("Enterd Number is ---> Equal to Zero")
# elif num%2==0:
#     print("Enterd Number is ---> Even Number")
# else:
#     print("Enterd Number is ---> Odd Number")


#------------------------------------------------------------------------------------------------------------------------------
    
"""Q28. Write a program to check if number is divisible by 2 and 3 but not 8.
"""
# num=int(input("Enter a Number : "))
# if num%2==0 and num%3==0 and num%8!=0:
#     print("Yes, Number is divisible by 2 and 3 but not 8.")
# elif num%2==0 and num%3==0 and num%8==0:
#     print("No, Number is divisible by 2 and 3 but also divisible with 8.")
# else:
#     print("No, but reason can't be specified.")

#------------------------------------------------------------------------------------------------------------------------------


"""

Q29. Write a program to print the last digit of a number. (NOT A IF ELSE QUESTION)

Example 1

Input: 45321

Output: 1

Example 2

Input: 459094

Output: 4

"""
# num = int(input("enter a number : "))
# l= num%10
# print(f"last digit of the number : {l}")

#------------------------------------------------------------------------------------------------------------------------------

"""Q30. Write a program to check if the last digit of a number is divisible by 5 or not.
"""
# num = int(input("Enter a Number : "))
# l= num%10
# print(f"Last Digit of the Number : {l}")
# if l==0:
#     print("No, Last Digit {l} is Not Divisible by 5.")
# elif l%5==0:
#     print("Yes, Last Digit {l} is Divisible by 5.")
# else :
#     print("No, Last Digit {l} is Not Divisible by 5.")

#------------------------------------------------------------------------------------------------------------------------------

"""
Q31. Write a program to calculate bill. Ask the final amount from the user.

You have to give discount and print the final bill after discount.

50000 above - 30% discount

40000-49999-25% discount

30000-39999-20% discount

10000-29999-10% discount

1-9999-No discount

Print the discount and the final amount to be paid.

Example 1

Enter bill amount = 80000

You got 30% discount

Your final bill is Rs. 56000

"""
# a = int(input("Enter bill amount : "))
# if a>=0 and a<10000:
#     print("You got No discount.")
#     print(f"Your Final Bill is Rs. {a}")
# elif a>=10000 and a<30000:
#     dm1 = a-((a*10)/100)
#     print("You got 10 % discount.")
#     print(f"Your Final Bill is Rs. {dm1}")
# elif a>=30000 and a<40000:
#     dm2 = a-((a*20)/100)
#     print("You got 20 % discount.")
#     print(f"Your Final Bill is Rs. {dm2}")
# elif a>=40000 and a<50000:
#     dm3 = a-((a*25)/100)
#     print("You got 25 % discount.")
#     print(f"Your Final Bill is Rs. {dm3}")
# elif a<=50000:
#     dm4 = a-((a*30)/100)
#     print("You got 30 % discount.")
#     print(f"Your Final Bill is Rs. {dm4}")
    
#------------------------------------------------------------------------------------------------------------------------------


"""Q32. Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.
"""
# n1=int(input("Enter the 1st Number : "))
# n2=int(input("Enter the 2st Number : "))
# n3=int(input("Enter the 3st Number : "))
# n4=int(input("Enter the 4st Number : "))

# if n1!=n2 and n1!=n3 and n1!=n4 and n2!=n3 and n2!=n4 and n3!=n4 :
#     if n1<n2 and n1<n3 and n1<n4:
#         print(f"1st Number {n1} is the smallest.")
#     elif n2<n1 and n2<n3 and n2<n4:
#         print(f"2st Number {n2} is the smallest.")
#     elif n3<n1 and n3<n2 and n3<n4:
#         print(f"3st Number {n3} is the smallest.")
#     else:
#         print(f"4st Number {n4} is the smallest.")
# else:
#     print("Some values are same, so try again with different Values.") 
        
        
        
#------------------------------------------------------------------------------------------------------------------------------
"""Q33. Ask a number from user

Print "Fizz" if the number is divisible by 3.

Print "Buzz" if the number is divisible by 5.

Print "FizzBuzz" if the number is divisible by 3 and 5.

Print the number itself if none of the conditions are true,

Below questions, do on your own.
"""

# num=int(input("Enter a Number : "))
# if num%3==0 and num%5==0:
#     print(f"FizzBuzz --- Because {num} is divisible by both 3 and 5.")
# elif num%3==0:
#     print(f"Fizz --- Because {num} is divisible by 3.")
# elif num%5==0:
#     print(f"Buzz --- Because {num} is divisible by 5.")
# else:
#     print(f"{num} , NO conditions are true for this number.")



#------------------------------------------------------------------------------------------------------------------------------

"""
Q34. A student will not be allowed to sit in exam if his/her attendance is less than 75%.

a. Take following input from user

1. Number of classes held

ii. Number of classes attended.

b. Print percentage of class attended

c. Print Is student is allowed to sit in exam or not.  
"""      









#------------------------------------------------------------------------------------------------------------------------------
"""Q35. Take Salary as input from User and Update the salary of an employee

⚫ salary less than 10,000, 5% increment

salary between 10,000 and 20, 000, 10% increment

⚫salary between 20,000 and 50,000, 15 % increment

salary more than 50,000, 20% increment"""



#------------------------------------------------------------------------------------------------------------------------------

"""Q36. Take three numbers as input from User and print which one is greater or are they equal.        
"""        



#------------------------------------------------------------------------------------------------------------------------------
        
"""       
Q37. An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. A leap year contains a leap day.

These are the conditions used to identify leap years:

if the year can be evenly divided by 4, it is then a leap year

but if the year is evenly divided by 4 and also by 100, then it is NOT a

leap year but if the year is evenly divided by 4 and also by 400, then it is a leap

year

This means the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Ask a year input from user. And tell if the year entered by user is leap or not

"""
        
# y=int(input("Enter a Year : "))
   
# if y>=0 and y<400:
#     if y%4==0 and y%100!=0:
#         print("it is a leep year.")
#     else:
#         print("not a leep year.")
# elif y>=400:
#     if y%4==0 and y%400==0:
#         print("it is a leep year.")  
#     else:
#         print("not a leep year.")
# else :
#     print("Invalid year, Enter a valid year and try again.")
        
        