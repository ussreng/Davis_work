n=int(input('Enter a number: '))
if n<=0:
  print('Invalid! Please enter again.')
else:
  for i in range(n):
    if i==0 or i==n-1:
      print('*'*n)
    elif i<n//2:
      print('*'+' '*(i-1)+'*'+' '*(n-2-2*i)+'*'+' '*(i-1)+'*')
    elif i==n//2:
      print('*'+' '*(i-1)+'*'+' '*(i-1)+'*')  
    else:
      print('*'+' '*(n-i-2)+'*'+' '*(2*i-n)+'*'+' '*(n-i-2)+'*')