# Program to create a dictionary where keys are numbers 1 to 10 and values are their squares
def create_square_dict():
    square_dict = {i: i**2 for i in range(1, 11)}  # Dictionary comprehension to create the dictionary
    return square_dict

# Main function
def main():
    square_dict = create_square_dict()
    print("Dictionary of numbers and their squares:")
    print(square_dict)

# Execute the program
main()

