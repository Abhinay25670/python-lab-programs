num=int(input("Enter any number:"))
sum=0
rem=0
while num>0:
    rem=num%10
    sum=sum+rem
    num//=10
print(sum)