"""Q92. Make your own list. Print the list in reverse.

...

my_list = [4, -98; "Code and Debug", 22.22, 100]

# Output

#100 22.22 "Code and Debug" -98 4
"""

# a=[23,44,56,5,6.5,"Vinit","Kumawat",98,99.99,100]
# print(f"original list is : {a}")
# l=len(a)

# print("Reverse list is : ")
# for i in range(-1,-(len(a)+1),-1):
#     print(a[i],end=" ")

#--------------------------------------------------------------------------------------------------------------------------------------

"""Q93. Make your own list. Print all the even numbers present in the list.

...


my_list = [51, 74, 85, 91, 52, 44]

#Output

#74 52 44
"""

# a=[22,34,55,78,98.99,45,12,34,12.12]
# print(f"list is : {a}")
# print("Even elements in the list are : ")
# for i in range(0,len(a)):
#     if a[i]%2==0:
#         print(a[i],end=" ")


#--------------------------------------------------------------------------------------------------------------------------------------


"""Q94. Make your own list. Print all the odd numbers present in the list. (Do on your own)
"""
# a=[23,33,45,12,2,34,45.66,23.34,44,67.56,66.65]
# print(f"List is : {a}")

# print("Odd elements in the list are : ")
# for i in range(0,len(a)):
#     if a[i]%2!=0:
#         print(a[i],end=" ")
        

#--------------------------------------------------------------------------------------------------------------------------------------

"""Q95. Make your own list. Print all the elements present at even index position.

...

my_list [51, "Anirudh", 85, 91.66, 52, 44, 108, 2001

#Output

#51 85 52 100
"""

# a=[12,13,23,34,34,56.66,34.2,12.2,23.2,32.1,1,2,3,45,6,8,9]
# print(f"Original list is : {a}")
# print("even index position elements are : ")
# for i in range(0,len(a)):
#     if i%2==0:
#         print(a[i],end=" ")


#--------------------------------------------------------------------------------------------------------------------------------------

"""Q96. Make your own list. Print the sum of all elements present in that list.

...

my_list = [51, 85, 91.66, 52, 44, 100, 200]

#Output

#623.66"""


# a=[12,13,23,34,34,56.66,34.2,12.2,23.2,32.1,1,2,3,45,6,8,9]
# print(f"Original list is : {a}")

# c=0
# for i in range(0,len(a)):
#     c+=a[i]
# print(f"Sum of the list is : {c}")






#--------------------------------------------------------------------------------------------------------------------------------------

"""Q97. Make your own list. Count the number of even numbers present in that list.

my_list = [51, 85, 91.66, 52, 44, 100, 2001

#Output

#4
"""
# a=[12,13,23,34,34,56.66,34.2,12.2,23.2,32.1,1,2,3,45,6,8,9]
# print(f"Original list is : {a}")

# c=0
# for i in range(0,len(a)):
#     if a[i]%2==0 :
#         c+=1
# print(f"Count of number of even numbers present in that list is : {c}")


#--------------------------------------------------------------------------------------------------------------------------------------

"""Q98. Make your own list. Count how many numbers are divisible by both 2 and 5 in that list. (Do on your own)

my_list

[51, 85, 91.66, 52, 44, 100, 2001

# Output

#2"""

# a=[12,13,23,34,34,56.66,34.2,12.2,23.2,32.1,1,2,3,45,6,8,9,100,500,1000]
# print(f"Original list is : {a}")

# c=0
# for i in range(0,len(a)):
#     if a[i]%2==0 and a[i]%5==0 :
#         c+=1
# print(f"Count of numbers are divisible by both 2 and 5 in that list is : {c}")


#--------------------------------------------------------------------------------------------------------------------------------------


"""Q99. Make your own list. Find the sum of all even numbers present in that list.

my_list [51, 85, 1748, 52, 44, 100, 2001

# Output

#2144"""

# a=[12,13,23,34,34,56.66,34.2,12.2,23.2,32.1,1,2,3,45,6,8,9,100,500,1000]
# print(f"Original list is : {a}")

# s=0
# for i in range(0,len(a)):
#     if a[i]%2==0:
#         s+=a[i]
# print(f"Sum of all even numbers present in that list is : {s}")



#--------------------------------------------------------------------------------------------------------------------------------------

"""Q100. Make your own list. Find the sum of all numbers divisible by 3 or 4. (Do on your own)

my_list = [51, 85, 1748, 52, 44, 100, 200]

# Output

# 2195"""

# a= [51, 85, 1748, 52, 44, 100, 200]
# print(f"Original list is : {a}")

# s=0
# for i in range(0,len(a)):
#     if a[i]%3==0 or a[i]%4==0:
#         s+=a[i]
# print(f"Sum of all numbers divisible by 3 or 4 is : {s}")




#--------------------------------------------------------------------------------------------------------------------------------------


"""Q101. Make your own list. Print how many positive and negative numbers are here. (Do on your own)

"""

# a= [51, -85, 17,-48, -52, 44, 100, 200,-2,-1,-4,0,1,2,3]
# print(f"Original list is : {a}")

# cp=0
# cn=0
# cz=0
# for i in range(0,len(a)):
#     if a[i]>0:
#         cp+=1
#     elif a[i]<0:
#         cn+=1
#     else:
#         cz+=1
# print(f"count of all positive numbers is : {cp}")
# print(f"count of all negative numbers is : {cn}")
# print(f"count of all 0's is : {cz}")


#--------------------------------------------------------------------------------------------------------------------------------------



"""Q102. Make your own list. Print the largest number present in that list.

my_list = [51, 85, 1748, 52, 44, 100, 200]

# Output

#1748"""



a= [51, 85, 1748, 52, 44, 100, 200]
print(f"Original list is : {a}")

max=a[0]
for i in range(0,len(a)):
    if max<a[i]:
        max=a[i]
print(f"largest number present in that list is : {max}")

#--------------------------------------------------------------------------------------------------------------------------------------


"""Q103. Make your own list. Print the smallest number present in that list. (Do on your own)
"""

# a= [51, 85, 1748, 52, 44, 100, 200]
# print(f"Original list is : {a}")

# max=a[0]
# for i in range(0,len(a)):
#     if max>=a[i]:
#         max=a[i]
# print(f"largest number present in that list is : {max}")







































