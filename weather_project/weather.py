import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'san_francisco.csv'

dates = []
highs = []
lows = []

with open(filename, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    print("CSV columns:", reader.fieldnames)

    for row in reader:
        try:
            date = datetime.strptime(row['Date'], '%Y-%m-%d')

            high = float(row['Max Temperature'])
            low = float(row['Min Temperature'])

        except (ValueError, KeyError, TypeError):
            continue

        dates.append(date)
        highs.append(high)
        lows.append(low)


# Plot the temperatures.
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Shade the area between the high and low temperatures.
ax.fill_between(
    dates,
    highs,
    lows,
    facecolor='blue',
    alpha=0.1
)

ax.set_title(
    "Daily High and Low Temperatures - San Francisco",
    fontsize=16
)

ax.set_xlabel('', fontsize=12)
ax.set_ylabel("Temperature (°F)", fontsize=12)

fig.autofmt_xdate()

plt.show()