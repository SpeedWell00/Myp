# Function to calculate the sum of a and b
def sum_ab(a, b):
    return a + b

# Function to calculate the difference of c and d
def diff_cd(c, d):
    return c - d

# Function to calculate the product of e and f
def prod_ef(e, f):
    return e * f

# Function to calculate the power of g raised to h
def power_gh(g, h):
    return g ** h

# Function to calculate the final expression
def calculate_expression(a, b, c, d, e, f, g, h):
    part1 = sum_ab(a, b)
    part2 = diff_cd(c, d)
    part3 = prod_ef(e, f)
    part4 = power_gh(g, h)
    
    # Ensure no division by zero occurs
    if part2 == 0:
        return "Error: Division by zero!"
    
    # Calculate the full expression
    result = (part1 / part2) + part3 - part4
    return result

def main():
    # Input values for the variables
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))
    d = float(input("Enter value for d: "))
    e = float(input("Enter value for e: "))
    f = float(input("Enter value for f: "))
    g = float(input("Enter value for g: "))
    h = float(input("Enter value for h: "))
    
    # Calculate the expression
    result = calculate_expression(a, b, c, d, e, f, g, h)
    
    # Output the result
    print(f"The result of the expression is: {result}")

# Call the main function to run the program
main()
