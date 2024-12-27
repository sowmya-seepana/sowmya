Num=int(input("enter the integer :"))
Rem=0
reversed_Num=0
while(Num!=0):
    Rem=Num%10
    reversed_Num=reversed_Num*10+Rem
    Num=Num//10
print("Reversed Numbe :",reversed_Num)