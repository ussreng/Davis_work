file_name=input('Enter the file name: ')

vowels='AEIOUaeiou'
with open(file_name, 'r') as file:
  content=file.read()

count=0
for ch in content:
  if ch in vowels:
    count+=1

print(f"The number of vowels in '{file_name}' is: {count}")    