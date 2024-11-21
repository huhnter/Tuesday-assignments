def row_sums(my_matrix: list) -> None:
    for row in my_matrix:
        # Calculate the sum of the elements in the current row
        row_sum = sum(row)
        # Append the sum as a new element in the row
        row.append(row_sum)
# Define a sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Apply the function
row_sums(matrix)

# Print the modified matrix
print(matrix)
