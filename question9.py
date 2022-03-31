# Find the First Maximum, Second maximum, Third maximum number from the List.
numbers=[12,2,-3,4,5,43,23,-11,44]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)
second_max = 0
i=0
while i<len(numbers):
    if numbers[i]>second_max:
        if numbers[i]!=max:
            second_max=numbers[i]
    i=i+1
print(second_max)
third_max=0
i=0
while i<len(numbers):
    if numbers[i]>third_max and second_max:
        if numbers[i]!=max and numbers[i]!=second_max:
            third_max=numbers[i]
    i=i+1
print(third_max)


