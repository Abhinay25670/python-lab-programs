def count_ele(l1):
    counts={}
    for ele in l1:
        if ele in counts:
            counts[ele]+=1
        else:
            counts[ele]=1
    return counts

l1 = []
num = int(input("Enter no of elements in list you need:"))
for i in range(num):
    print("Enter element")
    ele = int(input())
    l1.append(ele)
print(l1)
elem = count_ele(l1)
print(elem)

# count1 = dict(l1)
# for ele in l1:
#     if ele in count1:
#         count1[ele]+=1
        
# print(count1)