# Function to calculate the minimum of a list
def calculate_min(numbers):
    return min(numbers)

# Function to calculate the maximum of a list
def calculate_max(numbers):
    return max(numbers)

# Function to calculate the sum of a list
def calculate_sum(numbers):
    return sum(numbers)

# Main function to execute the task
def main():
    # Step 1: Take input from the user (comma-separated numbers)
    input_data = input("Enter numbers separated by commas: ")
    
    # Step 2: Convert input string to a list of numbers
    numbers = [float(num) for num in input_data.split(",")]
    
    # Step 3: Calculate the results
    minimum = calculate_min(numbers)
    maximum = calculate_max(numbers)
    total_sum = calculate_sum(numbers)
    
    # Step 4: Output the results
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
    print(f"Sum of values: {total_sum}")

# Run the main function
if __name__ == "__main__":
    main()
