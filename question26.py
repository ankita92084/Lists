# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22


test_list=[1, 1, 1, 64, 23, 64, 22, 22, 22]
a=[]
i=0
while i<len(test_list):
    j=0 
    count=0
    while j<len(test_list):
        if test_list[i]==test_list[j]:
            count=count+1
        j=j+1
        if count>=3:
            if test_list[i] not in a:
                a.append(test_list[i])
    i=i+1
print(a)

