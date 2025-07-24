import math
sequence=input("enter the sequence: ")
D=sequence.split(',')
q=[]
H=30
C=50
for i in D:
    q.append(int(math.sqrt((2*C*int(i))/H)))
    
print("the value of q is: ",q) 
print(','.join(map(str, q))) 
    