a=int(input("Enter a number: "))

if a %100 == 0:
    if a % 400 == 0:
        print(a, "is a leap year")
    else:
        print(a, "is not a leap year")
elif a % 4 == 0:
    print(a, "is a leap year")
else:
    print(a, "is not a leap year")
# The code checks if a given year is a leap year or not.