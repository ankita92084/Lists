# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])


number=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max_length=number[i]
while i<len(number):
    b= number[i]
    if b>max_length:
       max_length=b
    i+=1
print("maximum length list is: ",max_length)
number=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
minimum_length=number[i]
while i<len(number):
    b= number[i]
    if b<minimum_length:
       minimum_length=b
    i+=1
print("mininum length list is: ",minimum_length)

