
# {key1:value1,key2:value2,key3:value3,....keyN:valueN}

dict={
    "name":"Vinit",
    "Age":22,
    "gender":"male",
}
print(dict)
print(type(dict))

dict={
    "name":"Vinit",
    "Age":22,
    "gender":"male",
    "name":"dinesh" #if i use same key again then it will print latest upaded key value in the output.
}
print(dict)

dict={
    "name":"Vinit",
    "Age":22,
    "gender":"male",
    1:2,    #key can be int, float, str
    2:3, 
    3.9:[1,2,3,4,4],
#     [1,2,3,4,4]:[1,2,], # key can not be a list
#     [1,2,3,4]:55
    "[1,2,3,4,4]":[1,2,], # key can be a string of list
    "[1,2,3,4]":55
}
print(dict)
