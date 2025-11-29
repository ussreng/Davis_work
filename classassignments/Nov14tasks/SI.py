# to create a progran to calculate S.I by a function
def calculateSI(p,r,t):
    return (p*r*t)/100
p=eval(input('Enter Principal amount: '))
r=eval(input('Enter rate: '))
t=eval(input('Enter time: '))
ans=calculateSI(p,r,t) #calling a function
print('Required S.I is ',ans)
