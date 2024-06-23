data1=input()
list1=[int(x) for x in data1.split(',')]
print(list1)
count=len(list1)
for i in range(0,count):
    print(list1[i],end=" ")