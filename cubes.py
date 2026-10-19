import matplotlib.pyplot as plt

# Generate values from 1 to 5000.
x_values = list(range(1, 5001))

# Calculate the cubes.
y_values = [x**3 for x in x_values]

# Create a scatter plot with a colormap.
plt.scatter(
    x_values,
    y_values,
    c=y_values,
    cmap=plt.cm.Blues,
    s=10
)

# Add a color bar.
plt.colorbar(label="Cube of Value")

# Add a title and labels.
plt.title("Colored Cubes", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)

# Save and display the plot.
plt.savefig("colored_cubes.png")
print("Test plot saved successfully!")