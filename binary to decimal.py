binary_number = [1,0,0,1,1,0,1,1]
i=0
sum=0
power=0
rev=binary_number[::-1]
while i<len(binary_number):
    sum=sum+(rev[i]*(2**power))
    power+=1
    i+=1
print(sum)


