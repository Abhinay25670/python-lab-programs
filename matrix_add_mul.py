#ADDITION OF A MATRIX
def matrix_add(matrix_a,matrix_b):
    if len(matrix_a)!= len(matrix_b) :
        return "Matrices should be of same dimension"
    result = []
    for i in range(len(matrix_a)):
        row=[]
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j]+matrix_b[i][j])
        result.append(row)
    return result

#MULTIPLICATION OF A MATRIX
def matrix_mul(matrix_a,matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return "No of columns in matrix_a should be equal to the rown in matrix_b"
    result=[[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a)) ]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j]+= matrix_a[i][k]*matrix_b[k][j]
    return result

#COLUMNS AND ROWS OF A MATRIX
m= int(input('Number of rows for matrix A, m ='))
n = int(input('Number of columns for matrix A, n='))
p =int(input('Number of rows for matrix - B, p ='))
q= int(input('Number of columns for matrix B, q='))
matrix_a=[]
matrix_b=[]
print("Enter values for matrix --A")

for i in range (1,m+1) :
    row=[]
    for j in range (1,n+1):
        print("Entry in row:",i,"column:",j)
        row.append(int(input()))
    matrix_a.append(row)

print("Enter values for matrix - B")

for x in range (1,p+1) :
    row2=[]
    for y in range (1,q+1):
        print("Entry in row:",x, "column:",y)
        row2.append(int(input()))
    matrix_b.append(row2)

print(matrix_a)
print(matrix_b)

print("MATRIX ADDITION:")
print(matrix_add(matrix_a,matrix_b))
print("MATRIX MULTIPLICATION")
print(matrix_mul(matrix_a,matrix_b))