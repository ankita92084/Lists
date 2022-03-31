# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
output=[]
count=0
while i<len(input_list):
    j=input_list[i]
    if j not in output:
        output.append(j)
        count+=1
    i+=1
print("input",input_list)
print("count is ",count,":","output",output)
