def gen_div_by7and5(n):
    for num in range(n+1):
        if num%7==0 and num%5==0:
            yield num

try:
    n=int(input("Enter a value for n : "))
    result=gen_div_by7and5(n)
    print(",".join(map(str,result)))
except ValueError:
    print("Invalid input. please enter a valid integer for n. ")
    