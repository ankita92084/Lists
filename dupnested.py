a=[1,[1,4,3],2,[1,3,2],2,[4,6,9,9],9,9,9]
i=0
b=[]
while i <len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            # print(a[i][j],i,j)
            # b.append(a[i][j])
            j+=1
       
    else:
        # print(a[i],i)
        b.append(a[i])
    i+=1
print(b)
index=0
c=[]
while index<len(b):
    f=b[index]
    if f not in c:
        c.append(f)
    index+=1
print(c)

