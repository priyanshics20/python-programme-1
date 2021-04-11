# find frequency of characters in a string
n = input('')
char_number = {}
for i in n:
    if i in char_number:
        char_number[i] += 1
    else:
        char_number[i] = 1
print('count of all characters in',n, ':- ',char_number)        
