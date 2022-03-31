a=[1,0,2,5,0,4,0]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]<1:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1
print(c+b)

