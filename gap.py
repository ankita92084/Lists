a=[1,2,3,4,5,6,7,8,9,10]
i=0
j=20
k=30
b=[]
count=0
innercount=1
while i<len(a):
    if count==2:
        if innercount==1:
            b.append(j)
            innercount+=1
        elif innercount==2:
            b.append(k)
            innercount=1
        count=0
    b.append(a[i])
    count+=1
    i+=1
print(b)

