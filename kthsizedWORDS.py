str=input("enter the string to be modified")
k=int(input("size of each word"))
list=[]
m_list=str.split()
for i in m_list:
    if len(i)==k:
        list.append(i)
print("The words of size",k,"are",list)