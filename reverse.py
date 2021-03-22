n= int(input("enter sting"))
rev=0
r=0
while n > 0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("the reversed number is:",rev)
