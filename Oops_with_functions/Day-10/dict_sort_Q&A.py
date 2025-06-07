a = {"a": 1, "c": 4, "d": 2, "b": 3}
print(f"dict is : {a}")

print(f"sort by key: {sorted(a.items(), key=lambda x: x[0])}")
print(f"sort by key: {type(sorted(a.items(), key=lambda x: x[0]))}")
print(f"sort by value: {sorted(a.items(), key=lambda x: x[1])}")
