# Write a Python program to scramble the letters of string in a given list. 
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

orignal_list=['Python', 'list', 'exercises', 'practice', 'solution']
i=0
a=[]
while i<len(orignal_list):
    j=0
    while j<len(orignal_list[i]):
        b=orignal_list[i][0:2]
        c=orignal_list[i][2:len(orignal_list[i])]
        e=c+b
        a.append(e)
        j=j+1
        i+=1
print(e)
