# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8,6,6,6]
a=[]
i=0
while i<len(test_list):
    j=0 
    count=0
    while j<len(test_list):
        if test_list[i]==test_list[j]:
            count=count+1
        j=j+1
        if count>3:
            if test_list[i] not in a:
                a.append(test_list[i])
    i=i+1
print(a)





