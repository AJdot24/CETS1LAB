a=input("Enter 1st list of integer values seperated by ',' :")
b=input("Enter 2nd list ofinteger values seperated by ',' :")
a=a.split(',')
b=b.split(',')
a=list(map(int,a))
b=list(map(int,b))
la=len(a)
lb=len(b)
print("Checking length of lists......")
if la==lb:
    print("equal length")
else:
    print("not equal")

print("Checking Sum of both list......")
if sum(a)==sum(b):
    print("sum equal")
else:
    print("sum not equal")
    
print("Checking for same values of both list......")
count=0
for i in range(la):
    for j in range(lb):
        if(a[i]==b[j]):
            count+=1
            print(b[j])
if count==0:
    print("NO values found")
