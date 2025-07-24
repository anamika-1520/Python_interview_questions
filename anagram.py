def anagram(str1, str2):
     if sorted(str1)==sorted(str2):
         print("The strings are anagrams.")
     else:
         print("strings are not anagrams.")
str1 = input("Enter the first string: ")    
str2 = input("Enter the second string: ")
anagram(str1, str2)
