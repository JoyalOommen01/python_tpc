n=int(input("enter the no of socks"))
arr=[]
print("enter the size of socks")
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
setarr=list(set(arr))
c=0
for i in setarr:
    paircount=arr.count(i)
    c=c+int(paircount/2)
    
print(c)
