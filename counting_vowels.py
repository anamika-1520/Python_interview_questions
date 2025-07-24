# Function to count the number of vowels in a string
def count_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    flag=0
    for i in s:
        if i in vowels:
            if flag==i:
                continue
            else:
                count+=1
                flag=i
        else:
            pass
    return count
s=input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(s))