a=int(input("Enter an integer :"))
b=int(input("Enter another integer :"))
if a>b:
    temp=b
else:
    temp=a
    for i in range(1,temp+1):
        if((a%i==0)and(b%i==0)):
                gcd=i
        
print(gcd)
