d={
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 20,
    'f': 10,
}
unique_values=set()
for value in d.values():
    unique_values.add(value)
print("unique values are: ",sorted(list(unique_values)))

print(dict(sorted(d.items())))
for key, value in d.items():
    print(key, value)