file_name=input('Enter the file name: ')
with open(file_name, 'r') as file:
  content=file.read()

char_count=len(content)

print(f"The number of characters in {file_name} is: {char_count}")