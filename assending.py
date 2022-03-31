n = int(input("List length: "))
list1 = []
for i in range(n):
    x = int(input("Elements: "))
    if (i == 0) or (x > list1[- 1]):
        list1.append(x)
    else:
        pos = 0
        while pos < len(list1):
            if x <= list1[pos]:
                list1.insert(pos, x)
                break
            pos = pos + 1
print(list1)
