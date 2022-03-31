# List product excluding duplicates.
	# List = [6,1,3,5,6,3,1]
# 	Output: 60
list = [6,1,3,5,6,3,1]
i=0
a=[]
multi=1
while i<len(list):
    b=list[i]
    if b not in a:
        a.append(b)
        multi=multi*a[i]
    i+=1
print(a,"\n",multi)
    

