a=[12,2,3,43,23,11,44]
a.sort(reverse=True)
print(a[0]+a[1])
max=a[0]
max1=a[1]
for i in a:
    if i>max:
        max=1
for i in a:
    if i>max1:
        if i!=max:
            max1=1
print(max+max1)
i=0
b=[]
