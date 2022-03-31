a=[3,5,-1,4,6,-9,10]
b=[]
i=0
max=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
        b.append(max)
    else:
        b.append(max)
    i+=1
print(b)
