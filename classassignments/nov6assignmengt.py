a=float(input('Enter side 1: '))
b=float(input('Enter side 2: '))
c=float(input('Enter side 3: '))

if (a+b>c) and (b+c>a) and (c+a>b):
  print('The sides form a triangle')
  if a==b==c:
    print('It is an equilateral triangle')
  elif a==b or b==c or c==a:
    print('It is an isosceles triangle')
  else:
    print('It is a scalene triangle')
else:
  print('The sides does not form a triangle')          