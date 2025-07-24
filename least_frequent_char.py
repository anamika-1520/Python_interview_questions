s = "GeeksforGeeks"
dic={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i,j in dic.items():
    min=-1234354
    if dic[i]>min:
        min=dic[i]
    else:
        continue
print(min)    