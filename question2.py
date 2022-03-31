# Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest

original_list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(original_list):
    j=0
    while j<len(original_list[i]):
        print(original_list[i][j],end="")
        j+=1
    i+=1
    
    
