'''str1=input("enter the string 1: ")
str2=input("enter the string 2: ")
s1=(str1.split())
s2=(str2.split())
s3=[]
for i in range(len(s1)):
    if s2[i] not in s1:
        s3.append(s2[i])
for i in range(len(s2)):
    if s1[i] not in s2:
        s3.append(s1[i])
print("uncommon words are: ",s3)'''


str=input("enter the string : ")
lst=[]
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            if i not in lst:
                lst.append(str[i])
print("duplicate  words are: ",lst)

        
          
        