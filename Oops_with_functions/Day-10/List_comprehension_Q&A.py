x = int(input("X is : "))
y = int(input("Y is : "))
z = int(input("Z is : "))
n = int(input("N is : "))

result = [
    [i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1)
]
print(f"whole combinations are : {result}")

result = [
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
    if i + j + k != n
]
print(f"Answer is : {result}")
