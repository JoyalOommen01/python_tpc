a=int(input("enter a number"))
print("Factorial of",a,"is")
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
