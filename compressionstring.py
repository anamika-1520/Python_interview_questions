s='aaabbcccc'
l=list(s)
lst=[]
lsst={}
count=0
for i in l:
    if i in list(lst):
        lsst[i]+=1
    else:
        lsst[i]=1
    lst.append(i)
s=[]
    
for (i, j) in lsst.items():
    
    s.append(i)
    s.append(j)
print(''.join(str(i) for i in s)) 