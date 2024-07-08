# -*- coding: utf-8 -*-
"""Goemans-Williamson Max-Cut Algorithm

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19QKK8YJEJ0NsHjnjRVdtllX9cHm8m4bj
"""

t = 40
import networkx as nx
import random
G = nx.Graph()
G = nx.erdos_renyi_graph(t, 0.9)
nodes = G.nodes()
edges = G.edges()

import cvxpy as cp

X = cp.Variable((t,t), symmetric=True)

constraints = [X >> 0]
constraints += [
    X[i,i] == 1 for i in range(t)
]

objective = sum(0.5*(1 - X[i,j]) for (i,j) in edges)

prob = cp.Problem(cp.Maximize(objective), constraints)

prob.solve()

from scipy.linalg import sqrtm
x = sqrtm(X.value)

X.value

x

import numpy as np
u = np.random.randn(t)

u

x = np.sign(x@u)

x
