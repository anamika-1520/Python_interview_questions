s = "geeksforgeeks"
st=list()
re=''
for i in s:
    if i not in st:
        st.append(i)
        re=re+i
print(re)        
        
        