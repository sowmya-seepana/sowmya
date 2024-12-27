Num=int(input("enter the numbers ; "))
print("enter the odd numbers 1 to n :",Num," : ")
for i in range (1,Num+1):
    if(i%2!=0):
        print(i,end=' ')   