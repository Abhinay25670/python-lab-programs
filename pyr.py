def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        print((" ".join(map(str, row)).center(max_width)).rstrip())

# Take input from user until a valid input is entered
while True:
    num_rows = input("rows: ")
    if num_rows.isdigit() and int(num_rows) > 0:
        num_rows = int(num_rows)
        break
    
pascals_triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)
