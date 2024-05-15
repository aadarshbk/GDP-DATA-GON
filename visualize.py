import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file, ignoring lines with errors
data = pd.read_csv('data.csv')



# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create bar chart
bars = ax.barh(data['Category'], data['Percentage'], color='skyblue')

# Add labels, title, and grid
ax.set_xlabel('Percentage')
ax.set_ylabel('Category')
ax.set_title('Percentage Change by Category')
ax.grid(axis='x')

# Add value annotations on bars
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width:.2f}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords='offset points',
                ha='left', va='center')

# Show plot
plt.show()
