a=int(input("ENTER year: "))
if(a%400==0):
    print("leap Year")
elif(a%100!=0 and a%4==0):
    print("Leap year")
else:
    print("Not a leap year")
