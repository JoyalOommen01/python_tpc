n=int(input("enter the no people"))
input_array=[]
for i in range(0,n):
    input_=int(input("enter the input"))
    input_array.append(input_)
if input_array[0]==input_array[-1]:
    remaing=0
else:
    same=list(set(input_array))
    remaing=n-len(same)
print(remaing)
    
