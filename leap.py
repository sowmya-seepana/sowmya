Num=int(input("enter the year : "))
if(Num%4==0 and Num%100!=0)or (Num%400==0):
    print(Num,"it is a leap year")
else:
    print(Num,"it is not a leap year")