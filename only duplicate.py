l=[2,4,[9,1,7,[5,1,3],6,2,8]]
a=[]
i=0
while i<len(l):
    if type(l[i])==list:
        j=0
        while j<len(l[i]):
            if type(l[i][j])==list:
                k=0
                while k<len(l[i][j]):
                    a.append(l[i][j][k])
                    k+=1
            else:
                a.append(l[i][j])
            j+=1
    else:
        a.append(l[i])
    i+=1
print(a)
i=0
b=[]
while i<len(a):
    dup=a[i]
    if dup not in b:
        b.append(dup)
    i+=1
print(b)
