# Marian Remoroza
# CS2410 Data Science
# Program 2 - Python Visualization

'''Task 1'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('planets.csv')  # Initializing the list
df = pd.DataFrame(data)  # calling panda to input planets.csv into a data frame
# drawing a bar chart showing the density of planets
x = list(df.iloc[:, 0])
y = list(df.iloc[:, 3])

plt.bar(x, y, color='gold')
plt.title("Planets & Density")
plt.xlabel("Planets")
plt.ylabel("Density")
plt.show()

# drawing a pie chart showing the % of planets w/ -rotation val vs +rotation val
labels = 'Positive Rotation', 'Negative Rotation'
yp = list(df.iloc[:, 6])
colors = ['gold', 'lightcoral']
plt.pie(yp, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

# draw a line chart with x-axis as planets and y-axis as the gravity
yg = list(df.iloc[:, 4])
plt.plot(x, yg)
plt.xlabel("Planets")
plt.ylabel("Gravity")
plt.title("Planets & their Gravity")
plt.show()

# chart of my choice
day = list(df.iloc[:, 7])
plt.plot(x, day, color='lightcoral')
plt.xlabel("Planets")
plt.ylabel("Days")
plt.title("Planets & their corresponding Days")
plt.show()
