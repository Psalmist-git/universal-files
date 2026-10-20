import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 1. Initialize a new random walk and calculate the path
    rw = RandomWalk()
    rw.fill_walk()

    # 2. Map colors to the sequence of points (0 to 4999)
    point_numbers = list(range(rw.num_points))
    
    # 3. Plot the walk with a beautiful blue gradient tracking the path
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1) # Decreased size 's' to 1 for 5,000 points

    # 4. SAVE the chart to your folder BEFORE clearing it
    plt.savefig("rw_visuals.png", bbox_inches='tight')
    print("Test plot saved successfully as 'rw_visuals.png'!")

    # 5. CLEAR the canvas so the next walk starts completely fresh
    plt.clf()

    # 6. Check if the user wants to continue
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
