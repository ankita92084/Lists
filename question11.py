# For example, if we give 9119  the function should return  811181, as 
# the  square of 9 is 81 and square of 1  is 1.
num=(input("enter number:-"))
i=0
while i<len(num):
    print(int(num[i])*int(num[i]),end="")
    i+=1
print()


