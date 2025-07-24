s=input("enter the string: ")
s=s.lower()
'''count=0
for i in s:
    if i.isalpha():
        count+=1
        
if count>=26:
    print("The string is a pangram")
else:
    print("The string is not a pangram")'''

s=set(s)
alphabet=set("abcdefghijklmnopqrstuvwxyz")
if s>=alphabet:
    print("The string is a pangram")
else:
    print("The string is not a pangram")        
        