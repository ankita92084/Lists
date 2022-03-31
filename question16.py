# Write a Python program to find the difference between
#  elements (n+1th - nth) of a given list of numeric values.
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Difference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]



a=[1,2,3,4,5,6,7,8]
b=[]
c=1
i=0
while i<len(a) and c<len(a):
    d=a[c]-a[i]
    b.append(d)
    c+=1
    i+=1
print(b)








