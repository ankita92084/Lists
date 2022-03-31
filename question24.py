# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]


original_list = [1,2,3,1,2,2]
i=0
removed_list=[]
while i<len(original_list):
    j=original_list[i]
    if j not in removed_list:
        removed_list.append(j)
    i+=1
print("removed list is: ",removed_list)

