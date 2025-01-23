# Function to fill the matrix sequentially
def fill_matrix():
    matrix = [[0] * 6 for _ in range(6)]  # Create a 6x6 matrix initialized with zeros
    counter = 1
    for i in range(6):
        for j in range(6):
            matrix[i][j] = counter
            counter += 1
    return matrix

# Function to rotate the matrix 90 degrees clockwise
def rotate_matrix_90(matrix):
    n = len(matrix)
    # Create a new matrix for the rotated result
    rotated = [[0] * n for _ in range(n)]
    
    # Rotate the matrix 90 degrees clockwise
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    
    return rotated

# Function to print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()  # Add an extra line for spacing

# Main program
def main():
    # Step 1: Fill the matrix with values
    matrix = fill_matrix()
    
    # Step 2: Display the original matrix
    print("Original Matrix:")
    print_matrix(matrix)
    
    # Step 3: Rotate the matrix 90 degrees clockwise
    rotated_matrix = rotate_matrix_90(matrix)
    
    # Step 4: Display the rotated matrix
    print("Matrix after 90° Clockwise Rotation:")
    print_matrix(rotated_matrix)

# Run the program
if __name__ == "__main__":
    main()
