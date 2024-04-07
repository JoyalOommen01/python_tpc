def num_of_elements(n):
    num_ele=0
    while (n>0):
        num_ele+=1
        n=int(n/10)
    return num_ele
num=int(input("enter the number"))
print("no of elements=",num_of_elements(num))
