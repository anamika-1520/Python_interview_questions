def po(a):
    powset=[[]]
    s=[]
    for elm in powset:
        s.append(elm)
        powset.append(s+elm)
    return powset    
a=[1,2,3,4]
print(po(a))