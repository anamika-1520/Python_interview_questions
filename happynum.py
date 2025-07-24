num=int(input("Enter a number: "))
num1=num
sum1=0
for i in range(1, 100):
    sum = 0
    temp= num

    while temp > 0:
        sum1=sum
        digit = temp% 10
        sum += digit ** 2
        temp //= 10
    print("Sum of squares of digits of", i+1, "th step is", sum)
    if sum == 1:
        print(num1, "is a happy number")
        break
    if sum == sum1:
        print(num1, "is not a happy number")
        break
    num=sum
