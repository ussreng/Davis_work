source_file=input('Enter the source file: ')
dest_file=input('Enter the dest file: ')
with open('source_file', 'r') as src:
  data=src.read()
with open ('dest_file', 'w') as dest:
  dest.write(data) 
print('Data successfully copied')   