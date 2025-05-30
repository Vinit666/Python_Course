# named parameter---> using this we can give paramters to function without any order that is required by function
#                     or you can bypass the by default order to give parametr in function
def total_Marks(math, physic, chemistry, bio, hindi):
    print(f"your marks in math : {math}")
    print(f"your marks in physic : {physic}")
    print(f"your marks in chemistry : {chemistry}")
    print(f"your marks in bio : {bio}")
    print(f"your marks in hindi : {hindi}")
    total = math + physic + chemistry + bio + hindi
    print(f"your total marks is : {total}")


total_Marks(
    chemistry=80, math=70, bio=90, physic=100, hindi=30
)  # this is name parametr
print("\n")
total_Marks(
    80, 90, chemistry=80, bio=90, hindi=30
)  # if there is required parametrs then they all given first to function and then we will give all named parametrs

print("\n")


# default parameter function:--->take default value if user does not give values
def marks(math=0, physic=0, chemistry=0, bio=0, hindi=0):
    print(f"your marks in math : {math}")
    print(f"your marks in physic : {physic}")
    print(f"your marks in chemistry : {chemistry}")
    print(f"your marks in bio : {bio}")
    print(f"your marks in hindi : {hindi}")
    total = math + physic + chemistry + bio + hindi
    print(f"your total marks is : {total}")


marks(30, 40, 50, 60, 100)
print("/n")
marks(30, 40)

# def marks(math, physic, chemistry=0, bio=0, hindi=0):
#     print(f"your marks in math : {math}")
#     print(f"your marks in physic : {physic}")
#     print(f"your marks in chemistry : {chemistry}")
#     print(f"your marks in bio : {bio}")
#     print(f"your marks in hindi : {hindi}")
#     total = math + physic + chemistry + bio + hindi
#     print(f"your total marks is : {total}")


# marks(30, 40)
