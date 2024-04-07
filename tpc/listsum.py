li=[1,2,3,4,5,6,7,8,9,10]
sum=0
prd=1
for i in li:
    if (i%2==0):
        sum=sum+i
    else:
        prd=prd*i
print("sum =",sum)
print("prd =",prd)
