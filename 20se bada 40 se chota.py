numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
sum=0
while numbers[i:]:
    sum=numbers[i]
    if numbers[i]>=20 and numbers[i]<=40:
        print(sum)
    sum+=1
    i+=1
    