a={
    "name":"Vinit",
    "age":21,
    "gender":"male",
}
print(f"original dict is : {a}")

for i in a: #it will print only all keys
    print(i)

for i in a.items():
    print(i)    #it will print all key value pairs.

for k in a.keys():  #it will iterate in keys only.
    print(k)    
    
for v in a.values():    #it will iterate in values only.
    print(v)   

for k,v in a.items():
    print(f"{k} -> {v}")    #it will print all key value pairs.




#Q.
d={
    "history":76,
    "english":99,
    "math":90,
    "hindi":98,
    "physics":89
}

print(f"original dict is  : {d}")
t_m=0
for v in d.values():
    t_m+=v
print(f"total marks is : {t_m}")
    

print(f"original dict is  : {d}")
t_m=0
for k,v in d.items():
    t_m+=v
print(f"total marks is : {t_m}")
    






















