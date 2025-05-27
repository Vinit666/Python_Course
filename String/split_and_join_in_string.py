""" split() in string ---> it converts the string into list
"""
# str1="hii my name is vinit."
# print(f"string is : {str1}")

# m_list=str1.split() # split gives output as list --- and it split by default by space/(" ").
# print(m_list)


# str1="hii my name is vinit."
# print(f"string is : {str1}")

# m_list=str1.split("-") #string_name.split(it can be anyyhing,according to this it will split the string and make elements of list by this arg.)
# print(m_list)

# str1="-hii-my-name-is-vinit-.-"
# print(f"string is : {str1}")

# m_list=str1.split("-") 
# print(m_list)


"""join() in string ---> it again converts the list into string by joinig the list elements.
"""

# str1="-hii-my-name-is-vinit-.-"
# print(f"string is : {str1}")
# print(type(str1))

# m_list=str1.split("-") 
# print(f"string to list is : {m_list}")
# print(type(m_list))

# str2="-".join(m_list)
# print(f"list to again to string is : {str2}")
# print(type(str2))


# str1="-hii-my-name-is-vinit-.-12-15-%^^-%&-()-++"
# print(f"string is : {str1}")
# print(type(str1))

# m_list=str1.split("-") 
# print(f"string to list is : {m_list}")
# print(type(m_list))

# str2=" ".join(m_list)
# print(f"list to again to string is : {str2}")
# print(type(str2))


l=["hii","my" ,"name","vinit",45,88,"^^*9"]
str1=" ".join(str(i) for i in l)
print(f"list to again to string is : {str1}")
print(type(str1))

l=["hii","my" ,"name","vinit",45,88,"^^*9"]
str1=" ".join(str(i)[::-1] for i in l)
print(f"list to again to string is : {str1}")
print(type(str1))


