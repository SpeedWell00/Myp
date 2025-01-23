# Recursive function to calculate x^n
def power(x, n):
    # Base case: x^0 = 1
    if n == 0:
        return 1
    # Case when n < 0: we use the absolute value of n
    elif n < 0:
        return power(abs(x), n)  # We take the absolute value when n < 0
    # Case when n > 0: multiply x by the result of x^(n-1)
    else:
        return x * power(x, n - 1)

# Function to calculate the expression (x^k - x^m) / (x^k + x^m)
def calculate_expression(x, k, m):
    # Using the recursive power function
    xk = power(x, k)
    xm = power(x, m)
    
    # Calculate the expression
    numerator = xk - xm
    denominator = xk + xm
    
    # Handle the case where the denominator might be 0 to avoid division by zero
    if denominator == 0:
        return "Error: Division by zero"
    
    return numerator / denominator

# Main function to get input and output the result
def main():
    # Get user input for x, k, and m
    x = float(input("Enter the real number x: "))
    k = int(input("Enter the integer value k: "))
    m = int(input("Enter the integer value m: "))
    
    # Calculate and display the result
    result = calculate_expression(x, k, m)
    print(f"The result of the expression (x^k - x^m) / (x^k + x^m) is: {result}")

# Run the main function
if __name__ == "__main__":
    main()
