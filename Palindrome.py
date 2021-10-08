name=[ "m","o","m" ]
p=[]
i=1
while i<=len(name):
    print(name[-i])
    p.append(name[-i])
    i+=1
if p==name:
    print("palindrome")
else:
    print("not a palindrome")
    



