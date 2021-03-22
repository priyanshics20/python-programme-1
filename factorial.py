n = int(input('enter the number to find the factorial of that number '))
fact = 1
while n > 0 :
    fact *= n
    n -= 1
print(f'the factorial of given number  is {fact}')
