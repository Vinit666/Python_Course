#     for loop --- Q&A's

#------------------------------------------------------------------------------------------------------------------------------------


"""Q42. Ask a number from user. Print all the numbers from 1 to that number.
"""
# n=int(input("Enter the number you want to print from 1 : "))
# for i in range(1,n):
#     print(i,end=", ")
# print(n)

#------------------------------------------------------------------------------------------------------------------------------------

"""Q43. Ask a number (N) from user. Print all the numbers from N to 1.
"""
# n=int(input("Enter the number : "))
# for i in range (n,1,-1):
#     print(i,end=", ")
# print("1")

#------------------------------------------------------------------------------------------------------------------------------------

"""Q44. Ask start number and end number from user. Print all the numbers from start to end using for loop.
"""
# s=int(input("Enter the start point : "))
# e=int(input("Enter the end point : "))
# for i in range(s,e):
#     print(i,end=", ")
# print(e)

#------------------------------------------------------------------------------------------------------------------------------------
"""Q45. Calculate the sum of all the numbers from 1 to 10.
"""
# s=int(input("For sum enter the start point : "))
# e=int(input("Now enter the end point : "))
# count=0
# for i in range (s,e+1):
#     count+=i
# print(f"Sum of the all the numbers is : {count}")
    

#------------------------------------------------------------------------------------------------------------------------------------

"""Q46. Calculate product of all the numbers from 1 to 10.
"""
# s=int(input("For product enter the start point : "))
# e=int(input("Now enter the end point : "))
# p=1
# for i in range(s,e+1):
#     p*=i
# print(f"Product of the all the numbers is : {p}")







#------------------------------------------------------------------------------------------------------------------------------------

"""Q47. Calculate how many numbers are divisible by 7 from 1 to 100.
"""

# s=int(input("For check the divisible by 7, enter the start point : "))
# e=int(input("Now enter the end point : "))
# c=0
# for i in range(s,e+1):
#     if i%7==0:
#         c+=1
# print(f"divisible by 7 from all the numbers is : {c}")




#------------------------------------------------------------------------------------------------------------------------------------

"""Q48. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
"""
# s=int(input("For divisible by both 6 and 7, enter the start point : "))
# e=int(input("Now enter the end point : "))
# c=0
# for i in range (s,e+1):
#     if i%6==0 and i%7==0:
#         c+=1
# print(f"divisible by 7 from all the numbers is : {c}")






#------------------------------------------------------------------------------------------------------------------------------------

"""Q49. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
"""

# s=int(input("For divisible by 4, enter the start point : "))
# e=int(input("Now enter the end point : "))
# sum=0
# c=0
# for i in range (s,e+1):
#     if i%4==0:
#         c+=1
#         sum+=i
# print(f"Total numbers which are divisible by 4 are : {c}")
# print(f"Sum of all the numbers which are divisible by 4 is : {sum}")








#------------------------------------------------------------------------------------------------------------------------------------

"""Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
"""

# s=int(input("For divisible by both 6 and 7, enter the start point : "))
# e=int(input("Now enter the end point : "))
# c=0
# for i in range(s,e+1):
#     if i%6==0 and i%7==0:
#         c+=1
# print(f"divisible by 7 from all the numbers are : {c}")









#------------------------------------------------------------------------------------------------------------------------------------

"""
Q51. Ask a number from user. Print the multiplication table of that number

Example

Enter a number = 8

8x1=8

8 x 2 = 16
"""

# s=int(input("Enter a number to Show the multi. table : "))
# print(f"\nThe multiplication table of {s} is following : ")
# i=1
# for i in range(1,11):
#     m=s*i
#     print(f"{s}x{i} = {m}")



#------------------------------------------------------------------------------------------------------------------------------------

"""Q52. Calculate factorial of a number entered by user.

Example:

Enter a number = 5

Factorial of a number means product of all the numbers from 1 to that number.

5 factorial 5x4x3x2x1

Output = 120
"""

# n=int(input("Enter the number : "))
# f=1
# for i in range(n,0,-1):
#     f*=i
# print(f"The factorial of the number is : {f}")




#------------------------------------------------------------------------------------------------------------------------------------
"""Q53. Ask to numbers x and y from  the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.
"""

x=int(input("enter the value of x : "))
y=int(input("enter the value of y : "))
if x<y:
    for i in range(x,y):
        print(i,end=", ")
    print(y)
elif y<x:
    for i in range(y,x):
        print(i,end=", ")
    print(x)    
else:
    print("x and y Both are equal, Try again with different vales.")
    




#------------------------------------------------------------------------------------------------------------------------------------




































































