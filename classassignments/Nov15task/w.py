n=int(input('Enter a number: '))
if n<=0:
  print('Invalid! Please enter again.')
else:
  for i in range(n):
    if i==0:
      print('*'+' '*(2*n-2*i-3)+'*'+' '*(2*n-2*i-3)+'*')
    elif i==n-1:
      print(' '*i+'*'+' '*(2*i-1)+'*')
    else:
      print(' '*i+'*'+' '*(2*n-2*i-3)+'*'+' '*(2*i-1)+'*'+' '*(2*n-2*i-3)+'*')  