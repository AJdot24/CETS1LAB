a=input("Enter list of integers seperated by ',' :")
a=a.split(',')
a=list(map(int,a))
b=[x for x in a if x%2!=0]     
print(b)
