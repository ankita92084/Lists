# The task is to perform the operation of removing all the
#  occurrences of a given item/element present in a list.
#  Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2


occure=[1,1,2,3,4,5,1,2,1]
a=int(input("to remove"))
i=0
while i<len(occure):
    if occure[i]==a:
        occure.remove(occure[i])
        continue
    i+=1
print(occure)






