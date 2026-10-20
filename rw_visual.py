import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 1. Initialize a new random walk and calculate the path
    rw = RandomWalk()
    rw.fill_walk()

    # 2. Plot the points (adjust 's' for dot size)
    plt.scatter(rw.x_values, rw.y_values, s=15)

    # 3. Save the current walk to a file
    plt.savefig("rw_visuals.png")
    print("Test plot saved successfully!")

    # 4. CRITICAL FIX: Clear the figure canvas for the next iteration
    plt.clf()

    # 5. Check if the user wants to continue
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n': # .lower() handles accidental capital 'N'
        break
