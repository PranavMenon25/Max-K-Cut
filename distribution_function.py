# -*- coding: utf-8 -*-
"""Distribution Function

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ee-zCyefT3bQHqTVDQvRPuHN7clJQvFE
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np

num_of_nodes = 1000
beta = 1

plot = []
for i in range(num_of_nodes * 2 + 1):
  plot.append(0)

plot2 = []
for i in range(41):
  plot2.append([(i-20)/10, 0])

plot3 = []

new_var = 10000000
for i in range(new_var):
  rand_theta = (2 * random.random()) - 1
  rand_phi = random.randint(-1 * num_of_nodes, num_of_nodes)
  # print(rand_phi)
  func = math.tanh(rand_phi) - rand_theta
  func2 = func * 10 + 20
  plot3.append(func)
  # print(round(func2))
  plot2[round(func2)][1] = plot2[round(func2)][1] + 1
  if(func > 0):
    plot[rand_phi + num_of_nodes] = plot[rand_phi + num_of_nodes] + 1

for i in range(41):
  plot2[i][1] = plot2[i][1]/10000000

for i in range(num_of_nodes * 2 + 1):
  plot[i] = plot[i]/10000000
plt.plot(plot)
plt.xlabel('Phi + 100')  # Label for the x-axis
plt.ylabel('Number of switches')  # Label for the y-axis
plt.title('To not Switch Plot')  # Title of the plot
plt.grid(True)  # Adding grid for better readability

# Display the plot
plt.show()

x_values = [item[0]/10 for item in plot2]
y_values = [item[1] for item in plot2]
plt.plot(x_values, y_values)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.title('Plot of Array Elements')
plt.show()

import seaborn as sns
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xlabel('Phi + 100')  # Label for the x-axis
plt.ylabel('Number of switches')  # Label for the y-axis
sns.kdeplot(plot3, fill=True)

# from scipy.stats import norm
# mu, std = norm.fit(plot3)
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std)
# plt.plot(x, p, 'k', linewidth=2)

# # Adding labels and title
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.title('Probability Distribution of Randomly Generated Data')

# # Show the plot
# plt.show()

plot3

