a=input("Enter a string :")
a=a.upper()
l=len(a)
b=''
print(l)
count=0
c2=0
for i in range(l):
    #print(a[i])
    for j in range(l):
        #print(a[j])
        if (a[i])==(a[j]):
            count+=1         
    print("Occurs of %c is %d" %(a[i],count))
    if(count>1):
        c2+=1
    if c2==1:
        b+=a[i]
    elif c2>1:
        b+='$'
    #print(a[i])
    count=0
print(b)
