a=input("Enter String :")
a=list(a)
b=''
a[0],a[-1]=a[-1],a[0]
for x in a:
    b=b+x

print(b)
