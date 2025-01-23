import random

# Generate a 2D array with random numbers between 4 and 67
rows = 5  # Number of rows in the 2D array
cols = 4  # Number of columns in the 2D array

# Create a 2D array with random integers between 4 and 67
array = [[random.randint(4, 67) for _ in range(cols)] for _ in range(rows)]

# Display the original array
print("Original Array:")
for row in array:
    print(row)

# Bubble Sort for the last column
def bubble_sort_last_column(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare the last column elements of adjacent rows
            if arr[j][cols-1] > arr[j+1][cols-1]:
                # Swap rows if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sort the array based on the last column
bubble_sort_last_column(array)

# Display the sorted array
print("\nSorted Array (based on the last column):")
for row in array:
    print(row)
