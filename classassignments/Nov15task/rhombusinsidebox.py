n=int(input('Enter a number: '))
if n<=0:
  print('Invalid! Please enter again.')
else:
  for i in range(n):
    if i==0 or i==n-1:
      print('*'*n)
    elif i==1 or i==n-2:
      print('*'+' '*(n//2-1)+'*'+' '*(n//2-1)+'*')   
    elif i==n//2:
      print('*'*2+' '*(n-4)+'*'*2)
    elif i<n//2:
      print('*'+' '*(n//2-i)+'*'+' '*(2*i-3)+'*'+' '*(n//2-i)+'*')  
    else:
      print('*'+' '*(i-n//2)+'*'+' '*(2*(n-i-1)-3)+'*'+' '*(i-n//2)+'*')