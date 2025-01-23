def rotate_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    
    # Perform 90° counterclockwise rotation
    for i in range(n):
        for j in range(n):
            rotated_matrix[n-j-1][i] = matrix[i][j]
    
    return rotated_matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    # Create and fill the 6x6 matrix with integers from 1 to 36
    matrix = [[(i * 6) + j + 1 for j in range(6)] for i in range(6)]
    
    print("Original Matrix:")
    display_matrix(matrix)
    
    # Rotate the matrix 90° counterclockwise
    rotated_matrix = rotate_matrix(matrix)
    
    print("\nRotated Matrix (90° counterclockwise):")
    display_matrix(rotated_matrix)

# Call the main function to execute the program
main()
