str=input("enter the string : ")
lst=[]
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            if str[i] not in lst:
                lst.append(str[i])
print("duplicate  words are: ",lst)
            