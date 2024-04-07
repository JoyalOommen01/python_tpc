def sumof(n):
    sum=0
    rev=0
    while (n>0):
        rem=n%10
        sum=sum+rem
        n=int(n/10)
        rev=rev*10+rem
        
    return sum,rev
    

num=int(input("enter the number to get sum"))
sumd,reve=sumof(num)
print("sum of digits=",sumd)
print("reverse of digits=",reve)
