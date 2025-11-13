lst = list(map(int, input('Enter 10 numbers: ').split()))
first=second=third=float('-inf')
for num in lst:
  if num>first:
    third=second
    second=first
    first=num
  elif num>second and num!=first:
    third=second
    second=num
  elif num>third and num!=first and num!=second:
    third=num
print('Second Largest: ',second)
print('Third Largest: ',third)        