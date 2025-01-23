Task 1: Create a Matrix class with an output method

class Matrix:
    def _init_(self, matrix):
        # Initialize with a two-dimensional list (matrix)
        self.matrix = matrix

    def display(self):
        # Method to display the matrix
        for row in self.matrix:
            print(row)

# Example usage
matrix1 = Matrix([[1, 2], [3, 4]])
matrix1.display()

Task 2: Add a method to calculate the sum of two matrices

class Matrix:
    def _init_(self, matrix):
        # Initialize with a two-dimensional list (matrix)
        self.matrix = matrix

    def display(self):
        # Method to display the matrix
        for row in self.matrix:
            print(row)

    def add(self, other):
        # Method to add two matrices
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same size")
        
        # Matrix addition
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        
        return Matrix(result)

# Example usage
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
matrix1.display()

print("Matrix 2:")
matrix2.display()

# Adding matrices
sum_matrix = matrix1.add(matrix2)

print("Sum of Matrix 1 and Matrix 2:")
sum_matrix.display()
