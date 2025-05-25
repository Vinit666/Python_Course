"""
Q104. Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list. 
Display the final list as the output.

...

#Example

Input the length of the list: 4

Enter number = 7

Enter number 14

Enter number 21

Enter number 28

Answer [7, 14, 21, 28]
"""

#By append method --->  

# lol = int(input("Enter the lenght of the list : "))
# a=[]
# for i in range(0,lol):
#     v=int(input("Enter number : "))
#     a.append(v)
# print(f"List is : {a}")



# By insert method ---> 

# lol = int(input("Enter the lenght of the list : "))
# a=[]
# for i in range(0,lol):
#     v=int(input("Enter number : "))
#     a.insert(i,v)
# print(f"List is : {a}")






#--------------------------------------------------------------------------------------------------------------------------------
"""Q105. Create a list and prompt the user for an 'old number' followed by a 'new number. If the 'old number' exists in the list, replace it with the 'new number' provided by the user.

...

my list [5, 10, 15, 20, 157

Enter the old number: 15

Enter the new number: 25

Updated list: [5, 18, 25, 20, 25)"""

# a=[5, 10, 15, 20, 157]
# on=int(input("Enter the old number : "))
# nn=int(input("Enter the new number : "))
# for i in range(0,len(a)):
#     if a[i]==on:
#         a[i]=nn
# print(a)


#--------------------------------------------------------------------------------------------------------------------------------

"""Q106. Remove all the even numbers from the list.
"""

# a=[5, 10, 15, 20, 157,12,56,89,90,80,100]
# n=[]
# for i in range(0,len(a)):
#     if a[i]%2!=0:
#         n.append(a[i])
# print(f"After removing the even numbers from the list : {n}")

#--------------------------------------------------------------------------------------------------------------------------------

"""
Q107. Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered. (Do on your own).

...

my_list = [10, 15, 20, 25, 30]

Enter a number: 5

# OUTPUT [15, 25]

"""

# a = [10, 15, 20, 25, 30]
# na=[]
# print(f"List is : {a}")
# n=int(input("Enter a number : "))
# for i in range(0,len(a)):
#     if a[i]%n!=0:
#         na.append(a[i])
# print(f"Updated list is : {na}" )






#--------------------------------------------------------------------------------------------------------------------------------

"""Q108. Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even. Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.

...

my_list=[3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

# Output

Odd [3, 17, 35, 41]

Even [8, 12, 22, 30, 48, 50]
"""

ol=[3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
odd=[]
even=[]
for i in range (0,len(ol)):
    if ol[i]%2==0:
        even.append(ol[i])
    else:
        odd.append(ol[i])
print(f"Odd = {odd}")
print(f"even = {even}")









