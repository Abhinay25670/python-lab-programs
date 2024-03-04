num = int(input("Enter a number:"))
sum=0
temp=num
if num>0:
    for i in range (1,num):
        if num%i==0:
            sum=sum+i

if temp==sum:
    print(sum,"is a perfect number")
else:
    print(num,"is not a perfect number!")    
