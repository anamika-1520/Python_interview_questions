sequence= input("enter the sequence :")
digits=0
letters=0
for i in sequence:
    if i.isdigit():
        digits+=1        
    elif i.isalpha():
        letters+=1
print("the number of digits is: ",digits)
print("the number of letters is: ",letters)
