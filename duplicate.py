duplicate=[10,9,10,40,20,50,34,70,50]
i=0
e=[]
while i<len(duplicate):
    j=duplicate[i]
    if j not in e:
        e.append(j)
    i+=1
print(e)
