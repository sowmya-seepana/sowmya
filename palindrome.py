Num=int(input("enter the integer value :"))
Rem=0
reversed_Num=0
temp=Num
while(Num!=0):
    Rem=Num%10
    reversed_Num=reversed_Num*10+Rem
    Num=Num//10
if(temp==reversed_Num):
    print(temp," is a palindrome number")
else:
    print(temp,"is not a palindrome number")