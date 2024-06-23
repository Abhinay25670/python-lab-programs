rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
rows1 = int(input("Enter the number of rows: "))
cols2 = int(input("Enter the number of columns: "))

if rows==rows1 and cols==cols2:
    list1 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at ({i}, {j}): "))
            row.append(element)
        list1.append(row)

    list2 = []
    for m in range(rows1):
        rows24 = []
        for n in range(cols2):
            element1 = int(input(f"Enter element at ({m}, {n}): "))
            rows24.append(element1)
        list2.append(rows24)
    print(list1)
    print(list2)
    list5=[]
    for h in range(rows):
        rows45=[]
        for k in range(cols):
            rows45.append(list1[h][k] * list2[h][k])
        list5.append(rows45)
    print(list5)
else:
    print("Addition is not possible")
   
