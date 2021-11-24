a=int(input("Enter an integer :"))
rev=0
while a!=0:
    num=a%10
    rev=num+rev*10
    a=a//10
print(rev)
