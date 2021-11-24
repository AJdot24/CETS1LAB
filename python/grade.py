a=int(input("Sub1 mark(out of 100): "))
b=int(input("Sub2 mark(out of 100): "))
c=int(input("Sub3 mark(out of 100): "))
perc=((a+b+c)/300)*100
print("Sub1 mark= ",a,"/100")
print("Sub2 mark= ",b,"/100")
print("Sub3 mark= ",c,"/100")
print("Percentage= ",perc,"%")
if(perc>=85):
    print("Grade is: A")
elif(perc>=75):
    print("Grade is: B")
elif(perc>=65):
    print("Grade is: C")
elif(perc>=55):
    print("Grade is: D")
elif(perc>=45):
    print("Grade is: E")
else:
    print("FAIL")
    
