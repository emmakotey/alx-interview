#!/usr/bin/python3

# Define the pascal_triangle function that takes an integer n
def pascal_triangle(n):
    # Check if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the base row [1]
    triangle = [[1]]

    # Generate subsequent rows of the triangle
    for i in range(1, n):
        # Get the previous row of the triangle
        prev_row = triangle[i - 1]

        # Create a new row and start with 1 as the first element
        curr_row = [1]

        # Calculate the elements between the first and last elements of the row
        for j in range(1, i):
            # Add the adjacent elements from the previous row to get the current element
            curr_row.append(prev_row[j - 1] + prev_row[j])

        # Add 1 as the last element of the row
        curr_row.append(1)

        # Add the current row to the triangle
        triangle.append(curr_row)

    # Return the generated Pascal's triangle
    return triangle


# Define the print_triangle function to print the Pascal's triangle
def print_triangle(triangle):
    # Iterate over each row of the triangle
    for row in triangle:
        # Convert each element in the row to a string and join them with commas
        row_str = ",".join([str(x) for x in row])
        # Print the row in the desired format
        print("[{}]".format(row_str))


# Execute the code if the script is run directly
if __name__ == "__main__":
    # Generate Pascal's triangle with 5 rows and print it
    print_triangle(pascal_triangle(5))

