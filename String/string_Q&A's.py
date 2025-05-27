
"""Q132. Ask a string from user Count how many alphabets are there in that string.
"""

# # to find lenght of the string method-1
# a=input("Enter a string : ")
# print(f"Lenght of the string is : {len(a)}")

# # to find lenght of the string method-2
# a=input("Enter a string : ")
# c=0
# for i in a:
#     c+=1
# print(f"Lenght of the string is : {c}")

# # to find the only alphabets count in string
# a=input("Enter a string : ")
# c=0
# for i in a:
#     if i.isalpha():
#         c+=1
# print(f"Only numbers of alphabets in string is : {c}")


#--------------------------------------------------------------------------------------------------------------------------------
"""Q133. Ask a string from user. Count the number of uppercase and lowercase characters in that String.
"""

# a=input("Enter a string : ")
# cu=0
# cl=0
# for i in range(0,len(a)):
#     if a[i].isupper():
#         cu+=1
#     elif a[i].islower():
#         cl+=1
# print(f"Uppercase charcters in string is : {cu}")
# print(f"Lowercase charcters in string is : {cl}")


#--------------------------------------------------------------------------------------------------------------------------------

"""Q134. Ask a string from user. Convert all the alphabets to uppercase.
"""
# a=input("Enter a string : ")
# au=a.upper()
# print(f"String in uppercase is : {au}")



#--------------------------------------------------------------------------------------------------------------------------------

"""Q134. Ask a string from user. Convert all the alphabets to lowercase. (Do on your own)
"""

# a=input("Enter a string : ")
# al=a.lower()
# print(f"String in lowercase is : {al}")


#--------------------------------------------------------------------------------------------------------------------------------

"""Q135. Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and don't change the other letters. (Do on your own)
"""

# a=input("Enter a string : ")
# na=a.swapcase()
# print(na)


#--------------------------------------------------------------------------------------------------------------------------------

"""Q136. Count the number of spaces in a string entered by user.
"""
# a=input("Enter a string : ")
# c=0
# for i in a:
#     if i==" ":
#         c+=1
# print(f"count of space in string is : {c}")
    

#--------------------------------------------------------------------------------------------------------------------------------

"""
Q137. Ask a string from user. Print the count of how many alphabets, digits, spaces and symbols (everything else) are there in that string. (Do on your own)

"""

# a=input("Enter a string : ")
# print(f"string is : {a}")
# ca=0
# cd=0
# cs=0
# crall=0
# for i in a:
#     if i==" ":
#         cs+=1
#     elif i.isalpha():
#         ca+=1
#     elif i.isdigit():
#         cd+=1
#     else:
#         crall+=1
# print(f"count of spaces in string is : {cs}")
# print(f"count of alphabets in string is : {ca}")
# print(f"count of digits in string is : {cd}")
# print(f"count of symbols in string is : {crall}")





