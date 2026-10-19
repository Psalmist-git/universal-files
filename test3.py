import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Create a custom colormap.
my_colors = ['red', 'yellow', 'green']

my_cmap = LinearSegmentedColormap.from_list(
    'my_custom_cmap',
    my_colors
)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(
    x_values,
    y_values,
    c=y_values,
    cmap=my_cmap,
    edgecolor='black',
    s=40
)

plt.colorbar(label='Square of Value')

plt.title("Squares Using a Custom Colormap")
plt.xlabel("Value")
plt.ylabel("Square of Value")

plt.savefig("test3.png")
print("Test plot saved successfully!")