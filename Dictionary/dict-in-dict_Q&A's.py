""" Q.find the sum of each student and print.
"""
# students_data ={
#     "anirudh":{
#         "roll_number": 431,
#         "gender": "Male",
#         "physics": 78,
#         "chemistry":89,
#         "maths": 67,
#         },
#     "sanjay": {
#         "roll_number": 122,
#         "gender": "Female",
#         "physics": 90,
#         "chemistry": 75,
#         "maths": 82,
#         },
#     "raj": {
#         "roll_number": 786,
#         "gender": "Female",
#         "physics": 82,
#         "chemistry": 91,
#         "maths": 56,
#         },
# }
# print(f"original dict is : {students_data}\n")


# for k,v in students_data.items():
#     s=(students_data[k]["physics"]+students_data[k]["chemistry"]+students_data[k]["maths"])
#     print(f"{k} scored sum of : {s}")

#-------------------------------------------------------------------------------------------------------------------------------

"""Q. print sum of marks of each student. 
"""

# students_data={
#     "anirudh": {
#         "roll_number": 101,
#         "gender": "Male",
#         "marks": [78, 89, 67, 92, 54],
#     },
#     "sara": {
#         "roll_number": 202,
#         "gender": "Female",
#         "marks": [90, 75, 82, 68, 91],
#     },
#     "alex": {
#         "roll_number": 303,
#         "gender": "Female",
#         "marks": [82, 91, 56, 78, 69],
#     },
# }
# #method -1
# for k,v in students_data.items():
#     s=sum(v["marks"])
#     print(f"{k} scored sum of : {s}")

# #method -2
# for k,v in students_data.items():
#     s=0
#     for i in students_data[k]["marks"]:
#         s+=i
#     print(f"{k} scored sum of : {s}")
        
    


#-------------------------------------------------------------------------------------------------------------------------------

"""
Q. sum of students_data -> keys -> marks it means dict->dict->dict->sum
"""


students_data = {
    
    "anirudh": {
        "roll_number": 101,
        "gender": "Male",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "sara": {
        "roll_number": 102,
        "gender": "Female",
        "marks": {"physics": 90, "maths": 75, "chemistry": 82},
    },
    "alex": {
        "roll_number": 103,
        "gender": "Male",
        "marks": {"physics": 82, "maths": 91, "chemistry": 56},
    },
}

for k,v in students_data.items():
    sum=v["marks"]["physics"]+v["marks"]["maths"]+v["marks"]["chemistry"]
    print(f"{k} -> {sum} ")
        




