import re
# This program checks if a string contains any special characters
def check_special_characters(string):
    lst=r'[!@#$%^&*()_+{}|:"<>?`~\';,./]'
    if re.search(lst,string):
        return True
    else:
        return False

str=input("Enter a string: ")
if check_special_characters(str):
    print("The string contains special characters.")
else:
    print("the string does not contain the special characters.")

