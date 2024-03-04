num=int(input("Enter a number:"))
sum=0
temp=num
while num>0:
    rem=num%10
    sum=(sum*10)+rem
    num=num//10
print("reverse of number",temp,"is",sum)
