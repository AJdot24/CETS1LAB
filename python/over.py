a=input("Enter integer values seperated by ',' :")
a=a.split(',')
c=list(map(int,a))
print(type(c[3]))
l=len(c)-1
while l>=0:
    if c[l]>=100:
        c[l]='over'
    l-=1
print(c)
