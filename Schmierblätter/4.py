import matplotlib.pyplot as plt

# Example ship speeds
ship_speeds = [0, 10, 8, 2, 0]

# Plot histogram
plt.hist(ship_speeds, bins=[0, 2, 5, 8, 11], edgecolor='black')
plt.xlabel('Speed (knots)')
plt.ylabel('Number of ships')
plt.title('Histogram of Ship Speeds')
plt.show()
