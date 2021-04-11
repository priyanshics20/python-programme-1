#find the number of vowels,consonants,digits and white spaces in string.
n = input('enter a string :- ')
vowels = 0
digits = 0
whitespaces = 0
consonants = 0
n = n.lower()
for i in range (len(n)):
    if (n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
        vowels += 1
    elif (n[i]>='a' and n[i]<='z'):
        consonants += 1
    elif (n[i]== ' '):
        whitespaces += 1 
    else :
        digits += 1

print('vowels = ',vowels)
print('digits = ',digits)
print('whitespaces = ',whitespaces)
print('consonants = ',consonants)
