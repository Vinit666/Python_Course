"""
Q.85 print the following pattern ?

        * 
      * *
    * * *
  * * * *
* * * * *


"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
        
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
     
     
#--------------------------------------------------------------------------------------------------------   
"""
Q.86 print the following pattern ?

        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5


"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
        
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()
        
#--------------------------------------------------------------------------------------------------------   
"""
Q.87 print the following pattern ?

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
        
#     for k in range(1,i+1):
#         print("*",end=" ")
    
#     for l in range(1,i):
#         print("*",end=" ")
#     print()
       
# for i in range(1,10,2):
#     for j in range(i,9):
#         print("",end=" ")
        
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()     


#--------------------------------------------------------------------------------------------------------   
"""
Q.87 print the following pattern ?

       * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *


"""

for i in range(1,10,2):
    for j in range(i,9):
        print("",end=" ")
        
    for k in range(1,i+1):
        print("*",end=" ")
    print() 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(" ",end=" ")
        
    for k in range(1,(i*2)-2):
        print("*",end=" ")
    print() 


































