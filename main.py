

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to get user inputs for frequencies and phase shifts
def get_user_inputs():
    # User inputs for the angular frequencies and phase shifts
    omega1 = float(input("Enter angular frequency ω1 for horizontal motion: "))
    omega2 = float(input("Enter angular frequency ω2 for vertical motion: "))
    amplitude = float(input("Enter amplitude a: "))
    t1 = float(input("Enter phase shift t1 for horizontal motion: "))
    t2 = float(input("Enter phase shift t2 for vertical motion: "))
    return omega1, omega2, amplitude, t1, t2

# Function to calculate x and y at a given time t
def calculate_position(t, omega1, omega2, amplitude, t1, t2):
    x = amplitude * np.cos(omega1 * (t - t1))
    y = amplitude * np.cos(omega2 * (t - t2))
    return x, y

# Main function to animate the motion of the point
def animate_motion(omega1, omega2, amplitude, t1, t2):
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-amplitude - 1, amplitude + 1)
    ax.set_ylim(-amplitude - 1, amplitude + 1)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    
    point, = ax.plot([], [], 'bo', markersize=8)  # Point to animate
    
    # Function to update the point position
    def update(t):
        x, y = calculate_position(t, omega1, omega2, amplitude, t1, t2)
        point.set_data(x, y)
        return point,

    # Create the animation, updating every 50 milliseconds
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 500), interval=50)
    
    plt.title('Point with Independent Harmonic Oscillations')
    plt.show()

# Main entry point
if __name__ == "__main__":
    # Get user input for frequencies, amplitude, and phase shifts
    omega1, omega2, amplitude, t1, t2 = get_user_inputs()
    
    # Start the animation
    animate_motion(omega1, omega2, amplitude, t1, t2)
