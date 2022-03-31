li=[1,[2,3,4],2,[3,4,5,],3,[6,7,8]]
i=0
a=[]
sum=0
while i<len(li):
    if type(li[i])==list:
        j=0
        while j<len(li[i]):
            if type(li[i][j])==list:
                k=0
                while k<len(li[i][j]):
                    a.append(li[i][j][k])
                    sum=sum+(li[i][j][k])
                    k+=1
            else:
                a.append(li[i][j])
                sum=sum+li[i][j]
            j+=1
    else:
        a.append(li[i])
        sum=sum+li[i]
    i+=1
print(a)
print(sum)
            

