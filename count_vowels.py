
s1 = "VISHAKSHI"

count=0
v='aeiouAEIOU'

for i in s1:
    if i in v:
        count+=1
    else:
        continue
        
print(count)