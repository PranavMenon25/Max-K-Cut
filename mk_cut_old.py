# -*- coding: utf-8 -*-
"""MK Cut-old

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PRxdVhDZs6cq_HxSAVx-kTtWKc9ULs9w
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np
import random
import math

G = nx.Graph()
G = nx.erdos_renyi_graph(100, 0.3)
nodes = G.nodes()
edges = G.edges()
nx.draw(G, with_labels=True)
plt.show()

J = nx.to_numpy_array(G)



i = 0
j = 0
size = J.shape
for i in range(size[0]):
  for j in range(size[1]):
    if(J[i][j] == 1):
      J[i][j] = -1

def random():
  return np.random.randint(1,4)

states = []

for i in range(len(nodes)):
  state = random()
  # print(random())
  if(state == 1):
    p = np.array([1,0,0])
    states.append(p)
  elif(state == 2):
    p = np.array([0,1,0])
    states.append(p)
  else:
    p = np.array([0,0,1])
    states.append(p)

optimum_ans = states

def find_energy():
  energy = 0
  for i in range(G.number_of_nodes()):
    for j in range(i):
      energy = energy + J[i][j] * int(2*np.dot(states[i], states[j])-1)
  energy = -1 * (energy)
  return energy

find_energy()

def calc_phi(alpha):
  toRet = 0
  for i in range(G.number_of_nodes()):
    if(i != alpha):
      toRet = toRet + J[alpha][i] * (2*np.dot(states[i], states[alpha])-1)

  return toRet

#calc the distribution of switch
import random
toPlot = []
tryForOne = 100000
beta = 0.1
for i in range(-1*len(nodes), len(nodes)):
  switch = 0
  for j in range(tryForOne):
    rand_theta = (2 * random.random()) - 1
    # print(rand_theta)
    func = math.tanh(i * beta) - rand_theta
    if(func > 0):
      switch = switch + 1
  toPlot.append([i, (switch/tryForOne)])

x_values = [item[0] for item in toPlot]
y_values = [item[1] for item in toPlot]
plt.plot(x_values, y_values)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.title('Plot of Array Elements')
plt.show()

# New Approach

x1 = 0
x2 = 25
x3 = 50
x4 = 40

def func(phi, beta):
  rand_theta = (2 * random.random()) - 1
  fun = math.tanh(phi * beta) - rand_theta
  return fun

final = []
ph = 85
for i in range(10):
  # print(0.5 * (1 + np.sign(func(ph, 0.5))))
  # print(0.5 * (1 - np.sign(func(ph - x1, 0.5))) * (1 + np.sign(func(ph - x2, 0.5))) * (1 - np.sign(func(ph - x3, 0.5))) * 2)
  # print(0.5 * 3 * (1 - np.sign(func(ph - x2, 0.5))) * (1 - np.sign(func(ph - x3, 0.5))))
  # print(0.5 * 4 * (1 - np.sign(func(ph - x3, 0.5))))
  temp = (
        0.5 * (1 + np.sign(func(ph, 0.5))) +
        0.5 * (1 - np.sign(func(ph - x1, 0.5))) * (1 + np.sign(func(ph + x2, 0.5))) * (1 + np.sign(func(ph + x3, 0.5))) * 2 +
        0.5 * 3 * (1 - np.sign(func(ph - x2, 0.5))) * (1 + np.sign(func(ph + x3, 0.5))) +
        0.5 * 4 * (1 - np.sign(func(ph - x3, 0.5)))
    )
  final.append(temp)

final
