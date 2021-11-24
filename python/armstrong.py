a=int(input("Enter an integer :"))
temp=a
sum1=0
while a>0:
    num=a%10
    sum1=num*num*num+sum1
    a=a//10
if(temp==sum1):
    print("Armstrong")
else:
    print("not armstrong")
