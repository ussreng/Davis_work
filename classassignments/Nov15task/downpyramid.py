n=int(input('Enter a number: '))
if n<=0:
  print('Invalid! Please enter again.')
else:
  for i in range(n):
    print(' '*i+'*'*(2*n-1-2*i))