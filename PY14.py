a=input("Enter sequence of numbers with ',' seperating them: ")
a=a.split(',')
b=map(int,a)
a=tuple(b)
print(max(a))
