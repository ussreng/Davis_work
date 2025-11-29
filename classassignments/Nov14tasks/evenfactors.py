#create a program to print all even factors of given number by creating a function
def evenfactors(n):
  for i in range(1,n//2+1):
    if n%i==0 and i%2==0:
      print(i,end=' ')
  print('No Remains')  

num=int(input('Enter a number: '))
evenfactors(num)      