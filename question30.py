# Given a list of numbers, write a Python program to count
# positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

list1 = [2, -7, 5, -64, -14]
i=0
count=0
counter=0
while i<len(list1):
    if list1[i]>=0:
        count+=1
    else:
        counter+=1
    i+=1
print(count,"positive",counter,"negative")

