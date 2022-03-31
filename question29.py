#  Remove empty List from List		
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

original_list=[5, 6, [], 3, [], [], 9]
i=0
a=[]
while i<len(original_list):
    if  type(original_list[i])==int:
        a.append(original_list[i])
    i+=1
print(a)










