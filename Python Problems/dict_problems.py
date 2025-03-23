# WAP to find number of occurance in of each letter in a word
word=input()
dictionaryOfLetters={}
for letter in word:
    dictionaryOfLetters[letter]= dictionaryOfLetters.get(letter,0)+1
print(dictionaryOfLetters)
