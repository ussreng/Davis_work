# create a program to input a number and print its all factors 
def allfactors(n):
  for i in range(1,n//2+1):
    if n%i==0:
      print(i,end=' ')
  print(n)  

num=int(input('Enter a number: '))
allfactors(num)   