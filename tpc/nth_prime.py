import math
def is_prime(num):
    flag= True
    for i in range(2,int(math.sqrt(num))+1):
            if (num%i)==0:
                flag= False
                break
    return flag
n=int(input("enter the no of prime number needed"))
count=0
i=1
while(count<n):
    i=i+1
    if(is_prime(i)== True):
        count=count+1
print(n,"th prime number=",i)
    
    
