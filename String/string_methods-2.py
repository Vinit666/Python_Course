""" 
count(), Strtswith(), endswith(), 
Index(), find(), replace(), strip()
 
"""
#count()
s="python is good and course is very good."
print(s.count("o")) #output --->6

s="python is good and course is very good."
print(s.count("god"))   #output --->0

#startswith()
s="python is good and course is very good."
print(s.startswith("god"))  #output --->False

s="python is good and course is very good."
print(s.startswith("py"))  #output --->True

#endswithg()
s="python is good and course is very good."
print(s.endswith(" goo"))  #output --->False

s="python is good and course is very good."
print(s.endswith("ood."))  #output --->True

#Index()--->it will show erroe if char/substring not found in string.
s="python is good and course is very good."
print(s.index(" goo"))  #output --->9

# s="python is good and course is very good."
# print(s.index("god"))  #output --->ValueError: substring not found

#find()
s="python is good and course is very good."
print(s.find(" goo"))  #output --->9

s="python is good and course is very good."
print(s.find("god"))  #output --->-1

#replace()
s="python is good and course is very good."
print(s.replace("o","$"))  #output --->pyth$n is g$$d and c$urse is very g$$d.

s="python is good and course is very good."
print(s.replace("god","@"))  #output --->python is good and course is very good.

#strip()
s="  python    course                    n"
print(s.strip(" goo"))  #output --->python    course

s="@@ @@ @@@python@@@is @@@ good@@@@@@   @@@@"
print(s.strip("@"))  #output ---> @@ @@@python@@@is @@@ good@@@@@@
