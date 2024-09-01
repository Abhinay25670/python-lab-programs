str = input("Enter any string: ")
alpha=spl=digit=1
for i in range(len(str)):
    if str[i].isalpha():
        alpha+=alpha
    elif str[i].isdigit():
        digit+=digit
    else:
        spl+=spl
print("No of Ocuurences of aplhabets in string are:",alpha)
print("No of occurences of digits in string are:",digit)
print("No of occurences of special char in string are:",spl)