def func(num):
    if(num%2==0):
        funum= num*10
    else:
        funum= num*20
    return funum
print(func(func(3)))
