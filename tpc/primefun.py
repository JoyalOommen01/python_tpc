import math
def primefun(num):
    flag=0
    if(num==0 or num==1):
        print("number is not prime")
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if (num%i)==0:
                print("number is not prime")
                flag=1
                break
        if flag==0:
            print("number is prime")
numm=int(input("enter the number"))
primefun(numm)
