import sys
import csv
import matplotlib.pyplot as plt
import os

def generate_plot(csv_path):
    x_values = []
    y_values = []

    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            x_values.append(float(row['x']))
            y_values.append(float(row['y']))

    plt.plot(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('CSV Data Plot')
    plt.grid(True)

    # Define the path where the plot image should be saved
    plot_path = os.path.join(os.path.dirname(csv_path), 'plot.png')

    plt.savefig(plot_path)
    plt.close()

if __name__ == '__main__':
    csv_path = sys.argv[1]
    generate_plot(csv_path)

