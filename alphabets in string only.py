#remove all characters in a string except alphabet
n = input('Enter a string :- ')
string = ''
for i in n:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=95 and ord(i)<=122):
        string = string+i
print('Alphabets in string :- ',string)        
    
