'''sequence=input("Enter a sequence of numbers separated by spaces: ")
sequence = sequence.split()

words=set(sequence)
main_sorted_words=sorted(words)
print("The sorted sequence is:")
print(" ".join(main_sorted_words))'''

sequence=input("enter the sequence of words :")
sequence = sequence.split()
count=0

'''for i in range(len(sequence)):
    count=0
    for j in range(i,len(sequence)):
        if sequence[i]==sequence[j]:
            
            count+=1
    print(sequence[i], ":", count)'''
word_freq={}   
for word in sequence:
        word=word.strip('.?')
        word=word.lower()
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
for word, freq in word_freq.items():
    print(word, ":", freq)
    
        
        

        

        
    

