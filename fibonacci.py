num =int(input("num: "))
sum=0
list1=[]
a,b = 0,1
print(a)

list1.append(a)

for i in range (2,num):
    
    if b<num:
        print(b)
        list1.append(b)
        sum=a+b
        a=b
        b=sum
        
print(list1)

total =0
for j in range (0,len(list1),2):
    total+=list1[j]
print("sum of even elements",total)







# for i in range (2,num):
#     sum=a+b
#     a=b
#     b=sum
#     print(b)