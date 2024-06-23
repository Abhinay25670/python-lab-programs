x = int(input("x: "))
y = int(input("y: "))

# Iterate over the range from 1 to y
for i in range(1, y + 1):
    # Calculate the result
    result = x * i
    print(f"{x} * {i} = {result}")

    # Check if the current iteration exceeds 20
    
else:
    # Print a message if the loop completes without breaking
    if y>20:
        print("rows is limited to 20")
