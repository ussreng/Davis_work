from shapes import Cylinder,Cone,Cube,Cuboid,Sphere

import sys
def main():
  while True:
    #selcting shapes
    print("\n Select a shape: ")
    print('1. Cylinder')
    print('2. Cone')
    print('3. Cube')
    print('4. Cuboid')
    print('5. Sphere')
    print('6. Exit')

    choice=int(input('Enter your choice: '))
    if choice==6:
     print('Exiting program...')
     break
    if choice==1: # for cylinder
      r=float(input('Enter radius: '))
      h=float(input('Enter height: '))
      shape=Cylinder(r,h)
    elif choice==2: # for cone
      r=float(input('Enter radius: '))
      h=float(input('Enter height: '))
      shape=Cone(r,h)
    elif choice==3: # for cube
      a=float(input('Enter side: '))
      shape=Cube(a) 
    elif choice==4: # for cuboid
      l=float(input('Enter length: '))
      b=float(input('Enter breadth: '))
      h=float(input('Enter height: '))
      shape=Cuboid(l,b,h)  
    elif choice==5: # for sphere
      r=float(input('Enter radius: '))
      shape=Sphere(r)
    else:
      print('Invalid choice! Try again')  
      continue

    print('\n Select operation: ')  
    print('1. Curved Surface Area (CSA)')
    print('2. Total Surface Area (TSA)')
    print('3. Volume') 

    op=int(input('Enter your choice: '))

    if op==1: # for curved surface area
      print('CSA =',shape.calculateCSA())
    elif op==2: # for total surface area
      print('TSA =',shape.calculateTSA())
    elif op==3: # for volume
      print('Volume =',shape.calculateVolume())
    else:
      print('Invalid operation!')      




sys.exit(main())