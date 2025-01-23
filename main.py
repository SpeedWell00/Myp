import tkinter as tk

def square_number():
    try:
        # Get the value from the first text field and calculate its square
        number = float(entry1.get())
        result = number ** 2
        # Display the result in the second text field
        entry2.delete(0, tk.END)
        entry2.insert(0, str(result))
    except ValueError:
        # Handle invalid input
        entry2.delete(0, tk.END)
        entry2.insert(0, "Invalid input!")

# Create the main window
root = tk.Tk()
root.title("Square Calculator")

# First text field
label1 = tk.Label(root, text="Enter a number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# Button
button = tk.Button(root, text="Calculate", command=square_number)
button.pack()

# Second text field
label2 = tk.Label(root, text="Result:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Run the application
root.mainloop()
