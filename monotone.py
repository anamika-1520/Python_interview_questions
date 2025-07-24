def is_m(s):
    return s == sorted(s) or s == sorted(s, reverse=True)

list = list(map(int, input("Enter numbers separated by space: ").split()))
print("Monotone?" , is_m(list))
