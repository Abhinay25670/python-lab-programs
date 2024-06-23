# n=input()
# list1= [x for x in n.split(" ")]
# print(list1)
# print(sorted(list1,reverse=True))



# list1 = [map(int,input("nums = ").split(","))]
# list2 = []
# for i in range(len(list1)):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#     else:
#         print("true")
#         break
# if list1 == list2:
#     print("false")


import ast

nums = input("nums = ")
list1 = ast.literal_eval(nums)

list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
    else:
        print("true")
        break
if list1 == list2:
    print("false")