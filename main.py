def calculate_salaries():
    # Initialize a 2D array (8 workers x 5 days) to store the number of devices assembled
    M = [[0 for _ in range(5)] for _ in range(8)]
    
    # Get the cost of assembling one device
    cost_per_device = float(input("Enter the cost of assembling one device: "))
    
    # Collect data from the user
    for i in range(8):
        print(f"Enter the number of devices assembled by worker {i+1} for each day (5 days):")
        for j in range(5):
            M[i][j] = int(input(f"Day {j+1}: "))
    
    # Calculate the weekly salary for each worker and find the maximum number of devices assembled in a day
    max_devices_per_day = 0
    weekly_salaries = []
    
    for i in range(8):
        total_devices = sum(M[i])  # Sum up the devices assembled in 5 days
        salary = total_devices * cost_per_device  # Calculate the weekly salary
        weekly_salaries.append(salary)
        
        # Find the maximum number of devices assembled by this worker on any single day
        max_devices_per_day = max(max_devices_per_day, max(M[i]))
    
    # Output the results
    for i in range(8):
        print(f"Worker {i+1} - Weekly salary: ${weekly_salaries[i]:.2f}")
    
    print(f"The maximum number of devices assembled by any worker in a day is: {max_devices_per_day}")

# Call the function to run the program
calculate_salaries()
