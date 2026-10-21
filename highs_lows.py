import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get dates and high and low temperatures from file.
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except (ValueError, IndexError):
            print("Missing or invalid data:", row)

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Check the collected data.
print("Number of dates:", len(dates))
print("Number of high temperatures:", len(highs))
print("Number of low temperatures:", len(lows))

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=0.5, label='Highs')
plt.plot(dates, lows, c='blue', alpha=0.5, label='Lows')

plt.fill_between(
    dates, highs, lows,
    facecolor='blue',
    alpha=0.1
)

# Format plot.
plt.title("Daily High and Low Temperatures - 2014\nSitka, Alaska", fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.legend()

# Save the graph.
plt.savefig('sitka_highs_lows.png', bbox_inches='tight')
print("Graph saved as sitka_highs_lows.png")