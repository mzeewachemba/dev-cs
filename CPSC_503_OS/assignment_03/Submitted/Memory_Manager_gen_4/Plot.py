import pandas as pd
import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        pass

    # Function to plot optimization
    def plot_optimization(self, metrics_list):
        # Convert the list of SchedulerMetrics to a DataFrame
        data = [
            [metric.name, metric.avg_turn_t, metric.avg_wt, metric.cpu_utilization, metric.max_turnaround_time,
             metric.max_wait_time, metric.cpu_throughput]
            for metric in metrics_list
        ]

        df = pd.DataFrame(data, columns=["Scheduler", "Avg Turnaround Time", "Avg Waiting Time", "CPU Utilization (%)",
                                         "Max Turnaround Time", "Max Wait Time", "CPU Throughput"])

        # Plot the data
        ax = df.plot(kind="bar", figsize=(10, 6))
        plt.title("Scheduler Metrics")
        plt.ylabel("Metric")
        plt.legend(loc="upper right")
        plt.grid(axis="y")

        # Add value annotations to each bar
        for p in ax.patches:
            ax.annotate(f"{p.get_height():.2f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                        textcoords='offset points')

        # Display plot
        plt.show()

    def plot_fragmentation_metrics(self, metrics_list):

        # Extract x and y values from the data list
        x_values = [item[0] for item in metrics_list]
        y_values = [item[1] for item in metrics_list]

        # Plot the data
        plt.plot(x_values, y_values, marker='o')  # You can choose a different marker if needed
        plt.xlabel('X Time')
        plt.ylabel('Y Fragmentation Percentage')
        plt.title('Fragmentation Metrics over Time')
        plt.grid(True)
        plt.show()

    # Call the plot_optimization function with the metrics list
    # plot_optimization(metrics_list)
