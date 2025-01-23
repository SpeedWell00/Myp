Task 1: Print reciprocal if negative, square if positive

# Input the number
n = float(input("Enter a number: "))

# Check if the number is negative or positive
if n < 0:
    result = 1 / n  # Reciprocal for negative numbers
    print(f"The reciprocal of {n} is {result}")
elif n > 0:
    result = n ** 2  # Square for positive numbers
    print(f"The square of {n} is {result}")
else:
    print("The number is zero, no reciprocal or square exists.")

Task 2: Calculate the value of the function f(x)

# Input the value of x
x = float(input("Enter the value of x: "))

# Calculate the value of the function based on x
if x > 9:
    f_x = x ** 3 + 9
elif x < 9:
    f_x = 9 * x - 1
else:  # x == 9
    f_x = 720

# Print the result
print(f"The value of f(x) for x = {x} is {f_x}")
