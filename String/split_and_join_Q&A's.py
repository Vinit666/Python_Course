"""Q138. Write a program to reverse the order of words.

#Example 1

my_string = "Hello World"

#Output

World Hello

#Example 2

my_string="python is good"

#Output

good is python
"""

# # method-1
# my_string = "Hello World"
# print(f"string is : {my_string}")

# my_list=my_string.split()
# ms=" ".join(my_list[i] for i in range(len(my_list)-1,-1,-1))

# print(f"Reverse order of words is : {ms}")

# # method-2
# my_string = "Hello World"
# print(f"string is : {my_string}")

# my_list=my_string.split()
# my_list.reverse()
# ms=" ".join(my_list)
# print(f"Reverse order of words is : {ms}")


#--------------------------------------------------------------------------------------------------------------------------------

"""Q139. Write a program that accepts a string and capitalizes the first letter of each word while converting all other letters to lowercase.

#Example 1

my_string = "hello WORLD"

#Output

Hello World

#Example 2

my_string="python is good"

#Output

Python Is Good"""



# my_string = "python is good"
# print(f"string is : {my_string}")

# ms=my_string.title()
# print(f"After capitalizes the first letter of each word : {ms}")



#--------------------------------------------------------------------------------------------------------------------------------

"""Q140. Write a program that reverses each word in a sentence while maintaining the word order. For example, "Hello World" should become

"olleH dlroW"."""


# my_string = "Hello World"
# print(f"string is : {my_string}")

# my_list=my_string.split()
# ms=" ".join(i[::-1] for i in my_list)

# print(f"Reverse order of words is : {ms}")




#--------------------------------------------------------------------------------------------------------------------------------

"""Q141. Write a program that converts a string in camelCase to snake_case.

For example, converting "helloWorldHowAreYou" should result in "hello_world_how_are_you". (Do on your own)

"""



my_string = "helloWorldHowAreYou"
print(f"string is : {my_string}")

l=[]

c=0
for i in range(0,len(my_string)):
    if my_string[i].isupper():
        l.append(my_string[c:i])
        c=i
l.append(my_string[c:])

ms="_".join(i.lower() for i in l)
print(f"String in camelCase to snake_case is : {ms}")




