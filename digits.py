Num=int(input("enter the integer value : "))
digitcount=0
while(Num!=0):
    Num=Num%10
    digitcount=digitcount+1
print(digitcount,"digits")