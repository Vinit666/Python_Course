""" 
title(), capitalize(), upper(), lower(), swapcase(),
isupper(), islower(), isaplh(), isalnum(),  isspace(), isdigit() 

"""

a="hii, my name is VINIT KumawaT."
print(a)
b=a.title() # output--->Hii, My Name Is Vinit Kumawat.
print(b)

a="hii, my name is VINIT KumawaT."
print(a)
b=a.capitalize() # output--->Hii, my name is vinit kumawat.
print(b)

a="hii, my name is VINIT KumawaT."
print(a)
b=a.upper() # output--->HII, MY NAME IS VINIT KUMAWAT.
print(b)

a="hii, my name is VINIT KumawaT.1143#$^%#$^%90009"
print(a)
b=a.lower() # output--->hii, my name is vinit kumawat.1143#$^%#$^%90009
print(b)

a="hii, my name is VINIT KumawaT.1143#$^%#$^%90009"
print(a)
b=a.swapcase() # output--->HII, MY NAME IS vinit kUMAWAt.1143#$^%#$^%90009
print(b)

a="hii, my name is VINIT KumawaT.1143#$^%#$^%90009"
print(a)
b=a.isupper() # output--->False
print(b)

a="VINIT "
print(a)
b=a.isupper() # output--->True
print(b)

a="VINIT "
print(a)
b=a.islower() # output--->Flase
print(b)

a="hii,vinit "
print(a)
b=a.islower() # output--->True
print(b)

a="hii,vinit "
print(a)
b=a.isalpha() # output--->False
print(b)

a="hii vinit"
print(a)
b=a.isalpha() # output--->False
print(b)

a="hiivinit"
print(a)
b=a.isalpha() # output--->True
print(b)

a="hii vinit 343543"
print(a)
b=a.isalnum() # output--->False
print(b)

a="hiivinit343543"
print(a)
b=a.isalnum() # output--->True
print(b)

a="   ."
print(a)
b=a.isspace() # output--->False
print(b)

a="\n\t   "
print(a)
b=a.isspace() # output--->True
print(b)

a=" 54654661.4654  "
print(a)
b=a.isdigit() # output--->False
print(b)

a="5465 4654 "
print(a)
b=a.isdigit() # output--->False
print(b)

a="546546614654"
print(a)
b=a.isdigit() # output--->True
print(b)