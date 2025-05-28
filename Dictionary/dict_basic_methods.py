a={
    "name":"Vinit",
    "age":21,
    "gender":"male",
}
print(a)

# #accesing values 

# print(a["name"])
# print(a["namee"]) #if key does not exist then it will show error ---> KeyError: 'namee'



#using get() method --> if key not exist then print None that is a none datatype

# v=a.get("name")
# print(v)    #output--->Vinit

# v=a.get("namee") 
# print(v)    #output--->None



#adding or updating new key value pair dict.

# a["marks"]=100  #added new value if key does not exist. 
# print(a)    #output-->{'name': 'Vinit', 'age': 21, 'gender': 'male', 'marks': 100}

# a["age"]=10 #updaed value if key exist. 
# print(a)    #output-->{'name': 'Vinit', 'age': 10, 'gender': 'male', 'marks': 100}


# #removeing/deleting a key value pair from dict.

# del a["marks"]  #delet key value pair if exist. 
# print(a)    #output-->{'name': 'Vinit', 'age': 21, 'gender': 'male'}

# a.pop("gender") #delet key value pair if exist.
# print(a)    #output-->{'name': 'Vinit', 'age': 21}


#popitem()--->delets last key value pain in dict.
re=a.popitem()
print(re)

print(a)






