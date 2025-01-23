# Subroutine to input array elements from the keyboard
def input_array(n):
    array = []
    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        array.append(element)
    return array

# Subroutine to display array elements
def display_array(array):
    print("Array elements: ", end="")
    for element in array:
        print(f"{element:.2f}", end=" ")
    print()  # For newline

# Subroutine to calculate the arithmetic mean of positive elements
def mean_of_positive_elements(array):
    positive_elements = [x for x in array if x > 0]
    if positive_elements:  # Ensure that there are positive elements
        return sum(positive_elements) / len(positive_elements)
    else:
        return 0  # No positive elements

# Main subroutine
def main():
    n = 14  # Number of elements in each array
    
    # Input arrays A and B
    print("Enter elements for array A:")
    A = input_array(n)
    
    print("Enter elements for array B:")
    B = input_array(n)
    
    # Create array C where each element is min(A[k], B[k])
    C = [min(A[k], B[k]) for k in range(n)]
    
    # Display the arrays
    print("\nArray A:")
    display_array(A)
    
    print("Array B:")
    display_array(B)
    
    print("Array C:")
    display_array(C)
    
    # Calculate and display the mean of positive elements for each array
    mean_A = mean_of_positive_elements(A)
    mean_B = mean_of_positive_elements(B)
    mean_C = mean_of_positive_elements(C)
    
    print(f"\nArithmetic mean of positive elements in A: {mean_A:.2f}")
    print(f"Arithmetic mean of positive elements in B: {mean_B:.2f}")
    print(f"Arithmetic mean of positive elements in C: {mean_C:.2f}")

# Call the main function to execute the program
main()
