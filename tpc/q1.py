import math
def sum_noof(n):
    sum=0
    no_of=0
    while n>0:
        rem=n%10
        sum+=rem
        n=int(n/10)
        no_of=no_of+1
    return sum,no_of

def primefun(num):
    flag=True
    if(num==0 or num==1):
        flag= False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if (num%i)==0:
                flag=False
                break
    return flag
numm=int(input("enter the number"))
summ,num_of=sum_noof(numm)
if(primefun(summ)or primefun(num_of)):
    count=0
    i=1
    while(count<num_of):
        i=i+1
        if(primefun(i)== True):
            count=count+1
    print(num_of,"th prime number=",i)
else:
    sumsum,numnum=sum_noof(summ)
    print("sum of digits sum of digit =",sumsum)





    
