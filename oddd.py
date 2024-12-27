Num=int(input("enter the integer value : "))
oddigitcount=0
rem=0
while(Num==0):
    rem=Num%10
    if(rem%2==0):
        oddigitcount+=1
        Num=Num//10
print("number of odd digits are",oddigitcount)