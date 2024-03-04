num=int (input("Enter any number:"))
temp=num
sum=0
while num>0:
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
if(temp==sum):
    print(temp," is an Armstrong number")
else :
    print(temp," is not an Armstrong number")
