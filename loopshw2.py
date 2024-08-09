word=input('Enter a word:')
vowels='aeiouAEIOU'
length=len(word)
result=''
#for i in word:
 #   print(i)
counter=0
while counter<length:
    if word[counter] in vowels:
        #print('A vowel is present')
        pass
    else:
        #print('Vowels are not present')
        result+=word[counter]
    counter+=1
print(result)