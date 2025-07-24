a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

for i in range(a, b+1):
    if i>1:
        prime = True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime = False
        if prime==True:
            print(i, end=' ')
            # print(i)  # Uncomment this line if you want to print each prime number on a new line
     
        
# The code finds and prints all prime numbers between two user-defined integers a and b.
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# The code uses a nested loop to check each number in the range from a to b.
# The outer loop iterates through each number in the range, and the inner loop checks if the number is divisible by any number less than itself.
# If a number is found to be prime, it is printed; otherwise, the loop continues to the next number.
# The code is efficient for small ranges but may not be optimal for larger ranges due to the nested loop structure.
# The code can be optimized further by checking divisibility only up to the square root of the number.
# The code can also be improved by skipping even numbers greater than 2, as they cannot be prime.

# The code currently prints all prime numbers in a single line, separated by spaces.
# To print each prime number on a new line, you can uncomment the print(i) line.
# The code can be further optimized by checking divisibility only up to the square root of the number.
# The code can also be improved by skipping even numbers greater than 2, as they cannot be prime.
# The code currently prints all prime numbers in a single line, separated by spaces.
# To print each prime number on a new line, you can uncomment the print(i) line.
# The code can be further optimized by checking divisibility only up to the square root of the number.
# The code can also be improved by skipping even numbers greater than 2, as they cannot be prime.
# The code currently prints all prime numbers in a single line, separated by spaces.
