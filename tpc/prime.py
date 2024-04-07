import math
num=int(input("enter the number"))
flag=0
if(num==0 or num==1):
    print("number is not prime")

else:
    for i in range(2,int(math.sqrt(num))):
        if (num%i)==0:
            print("number is not prime")
            flag=1
    if flag==0:
        print("number is prime")
