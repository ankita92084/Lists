# Given 3 digits a, b, and c. The task is to find all 
# the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

L=[1,2,3]  
for i in range(3):
    for j in range(3):
        for k in range(3):                  
            if (i!=j and j!=k and i!=k):
                print(L[i], L[j], L[k])



