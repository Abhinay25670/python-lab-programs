# Read the number of elements
n = int(input("Input: "))

# Read elements separated by spaces in a single line
num_list = list(map(int,input().split()))
num_list=num_list[:n]

# Sort the list in reverse order
num_list.sort(reverse=True)

# Convert the sorted list to a string with spaces between elements
result = ' '.join(str(x) for x in num_list)

# Print the result with a space after the last element
print("Output:", result,end=' ')