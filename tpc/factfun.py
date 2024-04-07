def fact(num):
    facts=0
    for i in range(1,num+1):
        if((num%i)==0):
            print("factor=",i)
            facts=facts+1
    return facts
n=100
print("total factors=",fact(n))

