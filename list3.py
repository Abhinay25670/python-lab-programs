data = input("data: ")

list1 =[int(x) for x in data.split(',')]

print(list1)

print(sum(list1))

for i in range(len(list1)):
    list1[i] = list1[i]**2
print("squares: ",list1)