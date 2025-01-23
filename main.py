# Function to calculate the total weight lifted by each athlete
def calculate_totals(weights):
    totals = []
    for i in range(10):
        total = sum(weights[i])  # Sum the weights for each athlete
        totals.append(total)
    return totals

# Function to determine the winner
def find_winner(totals):
    max_weight = max(totals)
    winner_index = totals.index(max_weight)
    return winner_index, max_weight

# Main program
def main():
    # Initialize the 2D array M[10][3] with zeros
    M = [[0] * 3 for _ in range(10)]
    
    # Fill the array with user input
    print("Enter the weight lifted by each athlete in 3 events:")
    for i in range(10):
        for j in range(3):
            M[i][j] = float(input(f"Enter weight for athlete {i+1}, event {j+1}: "))
    
    # Calculate the total weight lifted by each athlete
    totals = calculate_totals(M)
    
    # Output the total weights lifted by each athlete
    print("\nTotal weight lifted by each athlete:")
    for i in range(10):
        print(f"Athlete {i+1}: {totals[i]} kg")
    
    # Find and output the winner
    winner_index, max_weight = find_winner(totals)
    print(f"\nThe winner is Athlete {winner_index+1} with a total weight of {max_weight} kg.")

# Run the program
if __name__ == "__main__":
    main()
