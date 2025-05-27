# t=(1,2,3,34,4,45,67,89)
# print(t)
# print(type(t))

# # tuple is immutable so we cant change, add, delete element in a tuple.
# t=(1,2,3,34,4,45,67,89)
# t[len(t)]=10 # it will show error ---> TypeError: 'tuple' object does not support item assignment
# print(t)


#acesssing the tuple elements
t=(1,2,3,34,4,45,67,89)
print(t[0])
print(t[-1])

#if you want to modify the tuple then convert it in list and do operations and then again convert it in the tuple.
t=(1,2,3,34,4,45,67,89)
print(t)    #print tuple

l=list(t)   #converted into list
print(l)  

l.append(10)   #added element in the list.
print(l)

t=tuple(l)  #again list converted into tuple
print(t)

