import re

s = 'My Profile: https://auth.geeksforgeeks.org/user/Rayyyy%20/articles in the portal of https://www.geeksforgeeks.org/'
pattern = r'https?://\S+|www\.\S+'

print("URLs:", re.findall(pattern, s))