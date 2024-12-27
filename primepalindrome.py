Num=int(input("enter the integer value :"))
Rem=0
reversed_Num=0
temp=Num
while(Num!=0):
    Rem=Num%10
    reversed_Num=reversed_Num*10+Rem
    Num=Num//10
if(temp==reversed_Num):
 for i in range(1,Num+1):
    if(Num%i==0):
       count=count+1
if(count==2):
     print("it is ap primepalindrome....!")
else:
   print("it is a primepalindrome........!")

