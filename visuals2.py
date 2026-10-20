import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 1. Generate a massive random walk (50,000 points)
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 2. Map colors to the sequence of points
    point_numbers = list(range(rw.num_points))
    
    # 3. Plot with ultra-fine dot sizes (s=1) to create the wispy look
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)

    # 4. MODERN FIX: Hide the axes, ticks, and borders completely
    plt.axis('off')

    # 5. Save the canvas to a file with tight borders
    plt.savefig("rw_art.png", bbox_inches='tight', dpi=300)
    print("Artistic plot saved successfully as 'rw_art.png'!")

    # 6. Clear the figure canvas so the next iteration starts clean
    plt.clf()

    # 7. Check if the user wants to continue
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
