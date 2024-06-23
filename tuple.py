list1=[i for i in range(1,31)]
print(list1)
list2=[]
for i in range(1,31):
    if i<6 or i>len(list1)-5:
        list2.append(i*i)
print(list2) 