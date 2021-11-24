a=input("Enter integer sepreated by ',':")
a=a.split(',')
b=list(map(int,a))
print(b)
c=[i for i in b if i>0]
print(c)
