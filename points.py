# Marian Remoroza
# CS2410 Data Science
# Program 2 - Python Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("5000_points.txt", header=None, names=['col1'])
print(df)
df['new_col'] = df['col1'].astype(str)

df['x'] = df['new_col'].str[4:10]
df['y'] = df['new_col'].str[14:20]
print(df)
df['x'] = df['x'].astype(int)
df['y'] = df['y'].astype(int)
x = df.x
y = df.y
# Draw a scatter graph to show all points.
plt.scatter(x, y, color='lightcoral')
plt.xlabel("x coordinates")
plt.ylabel("y coordinates")
plt.title("5000 Points")
plt.show()
