##4)Python Program to Find the Gravitational Force between Two Objects.
m1=float(input())
m2=float(input())
r=float(input())
G=6.673*(10**-11)
f=(G*m1*m2)/(r**2)
print("Hence, the gravitational force is: ",round(f,2),"N")
