n = input('enter a number to find that the number is armstrong or not  ')
ln = len(n)
s = 0
i = 0
while i<ln:
    s += int(n[i])**ln
    i += 1
if int(n) == s:
    print('the number is armstrong')
else:
    print('not armstrong')

