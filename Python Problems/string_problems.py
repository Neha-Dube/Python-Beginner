# WAP to reverse the conent of the string using slice operator

str= input("Enter the string to be reversed")
reverseStr=str[::-1]
print(reverseStr)

# WAP to reverse the string using reversed()

reverseUsingRfun=reversed(str)
print(reverseUsingRfun)
print(type (reverseUsingRfun))  # the type is of reversed type
#to make it of string type
outputStringTypeStr=''.join(reverseUsingRfun)
print(outputStringTypeStr)
print(type(outputStringTypeStr))

 #WAP to reverse the string using while loop

i=len(str)-1
reverseWhileStr=''
while i>=0:
    reverseWhileStr=reverseWhileStr+str[i]
    i=i-1
print(reverseWhileStr)

#WAP to reverse the order of the words in a string
