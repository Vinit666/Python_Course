"""
Q110. Make a list of your own. And remove all the duplicates element from that list.

my_list=[5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]

#OUTPUT [5, 1, "Code and Debug", 10, 20]

"""


# a=[5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]
# print(f"original list is : {a}")
# an=[]
# for i in range(0,len(a)):
#     if a[i] not in an:
#         an.append(a[i])
# print(f"\nUpdated list without duplicates is : {an}")







#--------------------------------------------------------------------------------------------------------------------------------
"""Q111. Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.

my_list=[5, 1, 5, 10, 20, 5, 1, 1]

Enter value = 10

#OUTPUT=3

Enter value = 5

OUTPUT 0

Enter value 160

OUTPUT-1"""

# a=[5, 1, 5, 10, 20, 5, 1, 1]
# print(f"List is : {a}")
# n=int(input("Enter the a number : "))
# for i in range(0,len(a)):
#     if n==a[i]:
#         print(f"index is : {i}")
#         break # usecase-1 ---> if u want only first element index that matches with the n then use this.
#               # usecase-2 ---> or if u want all indexes that matches element with n then don't use break statement.
#     elif n not in a:
#         print("-1")
#         break


#--------------------------------------------------------------------------------------------------------------------------------

"""0112. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

my_list=[5, 1, 5, 10, 20, 5, 1, 1]

Output

"""

# #method-1 --->
# a=[]
# rea=[]
# for i in range(1,11):
#     e=int(input(f"Enter the {i} integer : "))
#     a.append(e)    
# print(f"User Entered 10 integers list : {a}")

# a.reverse()
# rea=a
# print(f"Reverse list is : {rea}")



# #method-2 --->
# a=[]
# rea=[]
# for i in range(1,11):
#     e=int(input(f"Enter the {i} integer : "))
#     a.append(e)    
# print(f"User Entered 10 integers list : {a}")

# for i in range(len(a)-1,-1,-1):
#     rea.append(a[i])
# print(f"Reverse list is : {rea}")

#--------------------------------------------------------------------------------------------------------------------------------

"""
Q113. Write a program to find the average of all the numbers present in the list. (Do on your own)

"""

# a = [10, 15, 20, 25, 30]
# print(f"List is : {a}")
# avg=sum(a)/len(a)
# print(f"Averge of list is : {avg}" )


#--------------------------------------------------------------------------------------------------------------------------------

"""Q114. Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence.

"""

# ol=[1,2,3,4,1,2,1,2,3,4,2]
# print(f"Original list is : {ol}")
# wdl=[]
# cl=[]
# for i in range(0,len(ol)):
#     if ol[i] not in wdl:
#         wdl.append(ol[i])
# print(f"without duplicate list is : {wdl}")

# max_occ_ele=0
# max_occ=0
# for i in range (0,len(wdl)): 
#     c=0
#     for j in range (0,len(ol)): 
#         if wdl[i]==ol[j]:
#             c+=1 
#     if max_occ<c:
#         max_occ=c
#         max_occ_ele=wdl[i] 
#     cl.append(c)
# print(f"Count list is :  {cl}")
# print(f"Element value {max_occ_ele} have maximum occurence of {max_occ}")


#--------------------------------------------------------------------------------------------------------------------------------


"""Q115. Write a program that has two lists and make a new list that contains only the common elements between them without duplicates.

# Example 1

list1= [1, 2, 3, 4, 5]

list2 [3, 4, 5, 6, 7]

# Output

[3, 4, 5]

# Example 2

list1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 [5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

# Output

[5, 6, 7, 8, 9, 10]

"""

# l1 = [1, 2, 3, 4, 5, 3, 5]
# print(f"original list 1 : {l1}")

# l2 = [3, 4, 5, 6, 7]
# print(f"original list 2 : {l2}")

# nl = []
# wdfl=[]
# for i in range (0,len(l1)):
#     for j in range (0,len(l2)):
#         if l1[i]==l2[j]:
#             nl.append(l2[j])
# for k in nl:
#     if k not in wdfl:
#         wdfl.append(k)
    
# print(f"Merged list of list-1 and list-2 is : {wdfl}")

#--------------------------------------------------------------------------------------------------------------------------------

"""
Q116. Write a Python code to find the second largest element in a list without sorting.

"""
# # method-1 --->

# a = [10, 129, 20, 25, 30, 40, 639, 59, 298]
# print(f"List is : {a}")
# max=a[0]
# for i in range(0,len(a)):
#     if max<a[i]:
#         max=a[i]
# a.remove(max)
# semax=a[0]
# for i in range(0,len(a)):
#     if semax<a[i]:
#         semax=a[i]

# print(f"Second largest element in a list : {semax}")




# # method-2 --->

# a = [10, 129, 20, 25, 30, 40, 639, 59, 298]
# print(f"List is : {a}")

# l=float("-inf")
# sl=float("-inf")
# for num in a:
#     if num>l:
#         sl=l
#         l=num
#     elif num<l and num>sl:
#         sl=num
# print(f"Second largest element in a list : {sl}")




#--------------------------------------------------------------------------------------------------------------------------------

"""
Q117. Make a program that takes a list of integers and returns the product of all the elements.

"""

# a = []
# n = int(input("Enter the length of list : "))
# for i in range(1,n+1):
#     e=float(input(f"Enter the {i} Element : "))
#     a.append(e)
# print(f"List is : {a}")
# p=1
# for i in range(0,n):
#     p*=a[i]
# print(f"Product of all the elements in list is : {p}" )


#--------------------------------------------------------------------------------------------------------------------------------

"""
0118. Write a program to find and print all prime numbers within a given

man List= [12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 151]
"""

# a = [1,2,12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 151]
# print(f"List is : {a}")

# pl=[]
# for i in range(0,len(a)):
#     c=0
#     for j in range(1,a[i]+1):
#         if a[i]%j==0:
#             c+=1
#     if c==2:
#         pl.append(a[i])
# print(f"All prime numbers within a given list is : {pl}")






#--------------------------------------------------------------------------------------------------------------------------------

"""
Q119. Write a program to split a given list into two halves. (Do on your own)

"""

# a = [10, 15, 20, 25, 30, 30,20,10]
# print(f"Original list is : {a}")
# l1=[]
# l2=[]
# hl=int(len(a)/2)

# if len(a)%2==0:
#     for i in range(0,hl):
#         l1.append(a[i])
#     for j in range(hl,len(a)):
#         l2.append(a[j])
# else:
#     for i in range(0,hl+1):
#         l1.append(a[i])
#     for j in range(hl+1,len(a)):
#         l2.append(a[j])

# print(f"1st list is : {l1}" )
# print(f"2nd list is : {l2}" )


#--------------------------------------------------------------------------------------------------------------------------------

"""

0120. Write a program that swaps the first and last elements of a given list.

num_list = [32, 10, "Anirudh", 55.90, "xyz"]

Output

["xyz", 10, "Anirudh", 55.90, 32]

# Example 2

num_list = [100, 900]

# Output

[900, 100]
"""

a = [32, 10, "Anirudh", 55.90, "xyz"]
print(f"list is : {a}" )
temp=a[0]
a[0]=a[-1]
a[-1]=temp
print(f"Updated list is : {a}" )

# a = [32, 10, "Anirudh", 55.90, "xyz"]
# print(f"list is : {a}" )
# if len(a)>2:
#     a[0],a[-1]=a[-1],a[0]
# print(f"Updated list is : {a}" )





























































































