#declaring a function
def factorial(n):
  if n==0 or n==1:
    return 1
  fact=1
  for i in range(1,n+1):
    fact*=i
  return fact
# input from user
num=int(input('Enter a number: '))
ans=factorial(num)
print(f'Factorial of given number is: {ans}')
  