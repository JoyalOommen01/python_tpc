def fib(num):
    f=1
    s=1
    for i in range(1,num-1):
        t=f+s
        f=s
        s=t
    return s
    
        
n=int(input("enter the nth fib you want"))
print(fib(n))
