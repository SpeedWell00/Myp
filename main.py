import random

# Function to generate a random array of integers in the range {50, 100}
def generate_random_array(size):
    return [random.randint(50, 100) for _ in range(size)]

# Main function
def main():
    # Define the size of the array
    size = 20  # You can modify this to change the number of elements
    
    # Generate the random array
    random_array = generate_random_array(size)
    
    # Display the original array
    print("Original Array:")
    print(random_array)
    
    # Sort the array using Timsort (Python's built-in sort)
    sorted_array = sorted(random_array)
    
    # Display the sorted array
    print("\nSorted Array (Ascending Order):")
    print(sorted_array)

# Call the main function to execute the program
main()

