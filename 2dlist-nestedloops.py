# This code demonstrates the use of a 2D list and nested loops.

# What: A 2D list is a list of lists, allowing us to represent data in a grid-like format with rows and columns.
# When: 2D lists are used when we need to organize data in a grid or matrix, such as in applications involving tables, grids, or matrices.
# Why: They are particularly useful for tasks like representing game boards, storing matrices in mathematics, or working with image data.

# Define a 2D list named 'number_grid' containing four rows, each with a different number of elements.
number_grid = [
    [1, 2, 3],  # Row 1 with 3 columns
    [4, 5, 6],  # Row 2 with 3 columns
    [7, 8, 9],  # Row 3 with 3 columns
    [0]         # Row 4 with 1 column
]

# Nested loops are used to iterate over the elements of a 2D list.
# The outer loop ('for row in number_grid') iterates through the rows.
for row in number_grid:
    # The inner loop ('for col in row') iterates through the columns of each row.
    for col in row:
        # Printing each element in the grid.
        print(col)
