#!/usr/bin/python3

def pascal_triangle(n):
    '''
    Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []  # Initialize an empty list to store the triangle
    if type(n) is not int or n <= 0:  # Check if n is a positive integer
        return triangle  # Return an empty triangle if n is invalid
    for i in range(n):  # Iterate from 0 to n-1 to construct each row
        line = []  # Initialize an empty list for the current row
        for j in range(i + 1):  # Iterate from 0 to i to construct each element in the row
            if j == 0 or j == i:  # The first and last elements of each row are always 1
                line.append(1)
            elif i > 0 and j > 0:  # For other elements, calculate the sum of two elements from the previous row
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)  # Append the completed row to the triangle
    return triangle  # Return the Pascal's triangle as a list of lists

# Test the function
num_rows = 5
result = pascal_triangle(num_rows)  # Generate Pascal's triangle with 5 rows
for row in result:  # Iterate over each row in the triangle
    print(row)  # Print the row

