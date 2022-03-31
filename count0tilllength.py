a=[1,1,0,1,1,1,0,1]
b=[]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[j]==0  and j<i:
            count+=1
        if a[j]==1  and j>=i:
            count+=1

        j+=1
    b.append(count)
    i+=1
print(b)
    


