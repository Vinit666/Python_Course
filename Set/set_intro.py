"""
set={} 

--->set is used to store unique values.
--->unorderd
--->Mutable
--->Iteratable but not by index. because set in unorderd.

"""
my_set={12,23,4,5,45,7,6,34,34,34,32,22,12,3,4,5,6,7,8,"hello",12.34,12.34,1.2,2.1}
print(f"set is : {my_set}")
print(type(my_set))


# we can remove dublicates by usnig set to a list.
l=[12,23,12,1,1,1,2,2,2,3,3,3,4,4,45,5,5]   #this is a list
print(l)

my_set=set(l)   #list is converted to set and dublicates removesd by set.
print(my_set)

nl=list(my_set) #again convertd set to list and now list have the only uniques values and dublicates are reomved by set.
print(nl)

# union() in set : --->
set1={1,112,2,3,4,5,6,6,4,3,4,5,}
set2={1,12,23,4,33,43,45,3,354,55,534,36,63,6,3,36,6,4,3,4,5,}

print(set1.union(set2))


# intersection() --->
set1={1,112,2,3,4,5,6,6,4,3,4,5,}
set2={1,12,23,4,33,43,45,3,354,55,534,36,63,6,3,36,6,4,3,4,5,}

print(set1.intersection(set2))

# how to assign empty set--->

#by default this way of empty set is considerd dict by python.so we cant define a empty set like this.
set1={}
print(set1)     #output--->{}
print(type(set1))   #output---><class 'dict'>

#so we use set() to define a empty set.
set1=set()
print(set1)     #output--->set()
print(type(set1))   #output---><class 'set'>

# add() in sets
set1=set()
set1.add(120)
print(set1)

# remove() in set.
set1={12,23,4,5,5,6,7,7654,3,23,3,2,32,23,4,2,}
print(set1)

set1.remove(32)
print(set1)

set1.remove(7654)
print(set1)

set1={1,2,3,4,23,5,13,66,34,655,21,5,56,43,435,235,23,5,23,45,2,523,4,52,7,4,4,76,5,2,3,34,52,2,43}
print(set1)

n=int(input("Enter a number : "))
if n in set1:
    print("Yes")
else:
    print("No")
    
