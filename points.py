# Marian Remoroza
# CS2410 Data Science
# Program 2 - Python Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("5000_points.txt", header=None, names=['col1'])

df['new_col'] = df['col1'].astype(str)

df['x'] = df['new_col'].str[4:10]
df['y'] = df['new_col'].str[14:20]

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

# Draw a scatter graph that shows points in even position and odd position
df_even = df[['x', 'y']][::2]  # even
df_even.plot(
    x='x',
    y='y',
    kind='scatter',
    c='red',
    title='Even positions',
    xlabel='even x-axis',
    ylabel='even y-axis')
plt.show()

df_odd = df[['x', 'y']][1::2]
df_odd.plot(
    x='x',
    y='y',
    kind='scatter',
    c='green',
    title='Odd positions',
    xlabel='odd x-axis',
    ylabel='odd y-axis')
plt.show()

# draw a bar comparing the number of points in these three groups

# draw a chart of your choice
plt.plot(x, y)
plt.xlabel("X coorinates")
plt.ylabel("Y coordinates")
plt.title("Line Graph")
plt.show()
