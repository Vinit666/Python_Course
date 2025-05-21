"""

Q23. Write a Python program that takes an integer input and prints whether it's positive, negative. (Consider O as positive)

Q24. Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)

Q25. Write a program that takes two numbers as input and checks if the first number is divisible by the second.

Q26. A student will not be allowed to sit in exam if his/her attendance is less than 75%.


Take following input from user

Number of classes held

Number of classes attended.

1. Print percentage of class attended.

2. Print is student is allowed to sit in exam or not.

"""

#Q.23 solution ---> 

i=int(input("Enter the Number : "))
if i>=0:
    print("Number is Positive")
else:
    print("Number is negative")
    
#Q.24 solution --->

char=str(input("Enter the character from A-Z : "))
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("character is vowel")
else:
    print("Character is consonant")


#Q.25 solution --->
num1=int(input("Enter the 1st Number : "))
num2=int(input("Enter the 2nd Number : "))

if num1%num2==0:
    print("1st Number is Divisiable by 2nd Number")
else:
    print("1st Number is Not-Divisiable by 2nd Number")

#Q.26 solution --->
a=str(input("Enter the name of student : "))
hc=int(input("Enter the Number of classes held : "))
ac=int(input("Enter the Number of classes attended : "))
per=int((ac/hc)*100)
print("\nStudent Exam Status Report ---> ")
print(f"Name of Student : {a}")
print(f"Student attendence percentage : {per}")
if per>=75:
    print("Student is allowed to sit in exam.")
else:
    print("Student is Not-allowed to sit in exam.")

