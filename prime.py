Num=int(input("enter a integer :"))
count=0
for i in range(1,Num+1):
    if(Num%i==0):
        count+=1
if(count==2):
    print("prime number............!")
else:
    print("not a prime number.....!")
print("___________----------_---___________-----------------_______________")
for i in range(2,Num):
    if(Num%i==0):
        print("not a prime number.....!")
        break
    else:
      print("prime number............!")
    break
