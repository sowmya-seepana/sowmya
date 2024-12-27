stu_name=input("enter the stu_name :")
sub1=int(input("sub1 score:"))
sub2=int(input("sub2 score:"))
sub3=int(input("sub3 score:"))
total=0
average=0
print("student report :")
print("____________________________________")
print("student name :",stu_name)
print("subject1 :",sub1)
print("subject2 :",sub2)
print("subject3 :",sub3)
if(sub1>=35 and sub2>+35 and sub3>=35):
     total=sub1+sub2+sub3
     print("students total marks",total)
     average=(sub1+sub2+sub3)/(3)
     print("students average marks",average)
     if(average>=90):
      print("congratulations you have qualified in 1st class.....!")
     elif(average>=75):
        print("congratulations you have qualified in 2nd class.....!")
     else:
       print("congratulations you have qualified in 3rd class.....!")
else:
  print("better luck next time")
