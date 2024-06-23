# a,b,c = map(int,input("a,b,c: ").split(","))
# print(a,b,c)



n =int (input("n: "))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k=k+1
    print()