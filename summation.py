Num=int(input("enter the integer value :"))
sum_digits=0
rem=0
while(Num!=0):
    rem=Num%10
    sum_digits=sum_digits+rem
    Num=Num//10
print("sum of the digits are ",sum_digits)