num= int(input("Enter a number:"))
reverse_digits=[]
while num>0:
    digit=num%10
    reverse_digits.append(digit)
    num=num//10
print(reverse_digits)
    
