'''str=input("enter the string : ")
k=input("enter the element to be removed : ")
str1=""
for i in str:
    if i==k:
        continue
    str1=str1+i
print("The new string is",str1)'''
str=input("enter the string : ")
k =int(input(' enter the element to be removed : '))
str1=""
for i in range(len(str)):
    if k==i:
        continue
    str1=str1+str[i]
print("The new string is",str1)