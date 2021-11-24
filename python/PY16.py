a=input("Enter 1st string :")
b=input("Enter 2nd string :")
a=list(a)
b=list(b)
c=''
d=''
t1=a[0]
a[0]=b[0]
b[0]=t1
t2=a[1]
a[1]=b[1]
b[1]=t2
for x in a:
    c=c+x
for x in b:
    d=d+x

e=c+' '+d
print(e)

