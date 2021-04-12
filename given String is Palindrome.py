#Check if a given String is Palindrome
n = input('enter a string :- ')
rev = n[::-1]
if n == rev:
    print(n,'is equal to ',rev)
    print('Given string is palindrome')

else:
    print(n,'is not equal to',rev)
    print('Given string is not palindrome')

    
    
