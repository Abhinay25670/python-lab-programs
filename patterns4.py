n=5
for i in range(n):
    for j in range(0,n):
        if j==0 or i==j or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()
print()

n1=5
for i in range(7):
    for j in range(0,i):
        if  i==n1-1 or i+j>=n-3:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
