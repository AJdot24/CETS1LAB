a=['a','e','i','o','u','A','E','I','O','U']
b=input("Enter string:")
c=[i for i in b if i in a]
d=[]
d=[i for i in c if i not in d]
print(c)
