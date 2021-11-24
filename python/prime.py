a=int(input("Enter a number:"))
c=0
if a%1==0 and a%a==0:
    for i in range(2,a):
        if a%i==0:
            c+=1
if(c==0):
    print("prime")
else:
    print("Not prime")
    
