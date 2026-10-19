import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")

plt.title("My First Matplotlib Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig("my_graph.png")
print("Graph saved as my_graph.png")
