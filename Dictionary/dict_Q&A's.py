"""
Q142. Ask subject name and marks from the user and keep adding it to dictionary

...

Enter the number of subjects: 4

Enter the subject name: Maths

Enter the marks for Raths: 22

Enter the subject name: English

Enter the marks for English: 90

Enter the subject name: Computer

Enter the marks for Computer: 87

Enter the subject name: Science

Enter the marks for Science: 66

#Output ('Maths: 22.0, 'English': 90.0, 'Computer': 87.0, 'Science': 66.0)

"""

# s=int(input("Enter the number of subjects : "))
# d={}
# for i in range(1,s+1):
#         nk=(input("Enter the subject name : "))
#         nv=int(input(f"Enter the marks for {nk} : "))
#         d[nk]=nv    #method 1
#         # d.update({nk:nv})   #method 2
     
# print(f"new Dict is : {d}")


#-------------------------------------------------------------------------------------------------------------------------------

"""
Q143. Convert two lists into a dictionary. Make two list on your own of same length, and convert them to dictionary.

...

lst1= ['Ten', 'Twenty', 'Thirty']

1st2 [10, 20, 301

# Output

{'Ten': 10, 'Twenty': 20, 'Thirty': 30)

"""


# l1= ['Ten', 'Twenty', 'Thirty']
# print(f"List 1 is : {l1}")
# l2 =[10, 20, 30, ]
# print(f"List 2 is : {l2}")

# d={}

# for i in range(0,len(l1)):
#     d.update({l1[i]:l2[i]})
        

# print(f"New Dict is : {d}")




#-------------------------------------------------------------------------------------------------------------------------------


"""
Q144. Write a Python program to sum all the items in a dictionary.

"""


# m={
#     "hindi":78,
#     "english":76
# }
# #method 1
# s=0
# for v in m.values():
#     s+=v
    
# print(f"Sum of all value items in dict. is : {s}")

# #method 2
# print(f"Sum of all value items in dict. is : {sum(list(m.values()))}")



#-------------------------------------------------------------------------------------------------------------------------------

"""
Q145. Write a Python program to multiply all the items in a dictionary. (Do on your own)

"""

# d={
#     "hindi":9,
#     "english":4,
#     "math":10
# }
# p=1
# for v in d.values():
#     p*=v
# print(f"multiply all the value items in a dictionary is : {p}")


#-------------------------------------------------------------------------------------------------------------------------------

"""
Q146. Ask a string from user. Display the dictionary where each key is a character and value is the frequency of that character that comes in that string.

Enter a string: hello world

# Output

('h': 1, 'e': 1, '1': 3, 'o': 2, ': 1, 'w': 1, 'r': 1, 'd': 1
 
 """
 
# s=input("Enter a string : ")
# print(f"String is : {s}")
# d={}

# #method -1
# for i in range(0,len(s)):
#         v=s.count(s[i])
#         d.update({s[i]:v}) 
# print(f"Dict. is : {d}")

#method -2
# for i in range(0,len(s)):
#     v=s.count(s[i])
#     if s[i]!=d:
#         d.update({s[i]:v}) 
# print(f"Dict. is : {d}")


#-------------------------------------------------------------------------------------------------------------------------------

 
"""

Q147. Store "name" of a student as Key, "list of 5 marks" of that student as a Value. 
Store atleast 5 student names. 
Print the sum and percentage of all the students.

...

students dict(

"Student1": [85, 90, 78, 92, 88],.

"Student2": [75, 88, 92, 80, 87),

"Student3": [90, 95, 89, 78, 93],

"Student4": [80, 85, 88, 92, 87],

"Students": [92, 83, 95, 90, 55]

+

Studenti Sum: 433, Percentage: 86.60%

Student2 Sum: 422, Percentage: 84.40%

Student3 Sum: 445, Percentage: 89.00%

Student4 Sum: 432, Percentage: 86.40%

Students Sum: 450, Percentage: 90.00%


"""
# sd={}
# sn=int(input("Enter the numbers of students : "))

# for i in range(1,sn+1):
#     s_name=input("Enter the name of the student : ")
#     l=[]
#     for j in range(1,6):
#         s_m=int(input(f"Enter the {j} marks : "))
#         l.append(s_m)
#     sd.update({s_name:l})
# print(f"Student Record dictionary is : {sd}")


# for k,v in sd.items():
#     s=sum(v)
#     per=round((s/500)*100, 2)
#     print(f"{k} Sum of marks is : {s}, Percentage is : {per}%")
    


#-------------------------------------------------------------------------------------------------------------------------------

"""
Q148. Store marks of 5 different subjects in a dictionary. Ask subject name as an input from the User. 
Print the marks of that subject entered by User. If subject does not exist, print "Invalid".

"""

d={
    "hindi":89,
    "english":78,
    "math":79,
    "science":67,
    "history":93,
}
s=input("Enter the subject name : ")
if s in d:
    print(f"Marks of {s} is : {d.get(s)}")
else:
    print("Invalid subject name!")









