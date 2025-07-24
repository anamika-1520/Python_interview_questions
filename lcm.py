#code to calculate LCM of two numbers
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))   

if x>y:
    greater=x
else:
    greater=y
while True:
    if greater%x==0 and greater%y==0:
        lcm=greater
        break
    greater+=1
print("LCM of",x,"and",y,"is",greater)


# Function to calculate LCM of two numbers
import math
def lcm(x,y):
    return abs(x*y)//math.gcd(x,y)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("LCM of",x,"and",y,"is",lcm(x,y))

# Function to calculate LCM of three numbers
def lcm(x, y,z):
    lcm_xy=abs(x*y)//math.gcd(x,y)
    lcm_xyz=abs(lcm_xy*z)//math.gcd(lcm_xy,z)
    return lcm_xyz
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))
print("LCM of",x,"and",y,"and",z,"is",lcm(x,y,z))    