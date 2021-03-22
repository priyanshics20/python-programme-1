n = int(input('enter a number to check the number is prime or not '))
i = 2
while i < n:
    if n % i == 0:
        print('the number', n, 'is not prime number')
        break
    i += 1
else:
    print('the number', n, 'is prime number')