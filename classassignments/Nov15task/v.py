n=int(input('Enter a number: '))
if n<=0:
  print('Invalid! Please enter again.')
else:
  for i in range(n):
    if i==n-1:
      print('*'*(2*n-1))
    else:
      print('*'*(i+1)+' '*(2*n-3-2*i)+'*'*(i+1))