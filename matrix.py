m = int(input('Number of rows for matrix A, m ='))
n = int(input('Number of columns for matrix A, n='))
p =int(input('Number of rows for matrix - B, p ='))
q= int(input('Number of columns for matrix B, q='))
matrix_a=[]
matrix_b=[]
print("Enter values for matrix --A")
for i in range (1,m+1) :
    for j in range (1,n+1):
        print("Entry in row:",i,"column:",j)
        matrix_a.append(int(input()))

print("Enter values for matrix - B")
for x in range (1,p+1) :
    for y in range (1,q+1):
        print("Entry in row:",x, "column:",y)
        matrix_b.append(int(input()))
for i in range(1,m+1):
    for j in range(1,n+1):
        print(matrix_a[i][j])
print("Matrix_b = ",matrix_b)


