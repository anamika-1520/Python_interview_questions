sequence=input("Enter a sequence of numbers separated by spaces: ")
sequence = sequence.split(',')
l='$#@'
valid=[]
# Convert the sequence to a list of integers
for i in sequence:
    if len(i)>=6 and len(i)<=12:
       if  any(char.isalnum() for char in i) or any(char in i for char in l):
           valid.append(i)
    
       else:
           continue  
       
print(valid)