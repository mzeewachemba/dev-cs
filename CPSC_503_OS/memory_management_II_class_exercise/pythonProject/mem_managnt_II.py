import matplotlib.pyplot as plt

# Data
frames = [1, 2, 3, 4, 5, 6, 7]
fifo_faults = [20, 18, 16, 14, 10, 10, 7]
lru_faults = [20, 18, 15, 10, 8, 7, 7]
optimal_faults = [20, 15, 11, 8, 7, 7, 7]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(frames, fifo_faults, label='FIFO', marker='o')
plt.plot(frames, lru_faults, label='LRU', marker='o')
plt.plot(frames, optimal_faults, label='Optimal', marker='o')

# Adding titles and labels
plt.title('Page Faults vs. Number of Frames')
plt.xlabel('Number of Frames')
plt.ylabel('Number of Page Faults')
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
