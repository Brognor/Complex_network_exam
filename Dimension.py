import networkx as nx
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import numpy as np


#G = nx.erdos_renyi_graph(100, 0.1) test
l_b_max = nx.diameter(G)


def G_prime(G, l_B):
    G_prime = nx.Graph()
    N_prime = len(G.nodes)
    G_prime.add_nodes_from(G)
    E_prime = []
    for n1 in range(N_prime):
        for n2 in range(N_prime):
            try:
                if nx.shortest_path_length(G, n1, n2) > l_B:
                    G_prime.add_edge(n1, n2)
            except nx.NetworkXNoPath:
                return 0
    return G_prime


def Greedy_coloring(G):
    d = nx.coloring.greedy_color(G, strategy="random_sequential")
    return d


def dimension(G, l_b_max):
    N_bs = np.zeros(l_b_max)
    l_bs = np.zeros(l_b_max)
    for l_b in range(1, l_b_max, 1):
        G1 = G_prime(G, l_b)
        d = Greedy_coloring(G1)
        N_b = len(set(d.values()))
        N_bs[l_b] = N_b
        l_bs[l_b] = l_b
    l_bs = l_bs.reshape(-1, 1)
    model = LinearRegression().fit(l_bs, N_bs)
    dim = -model.coef_
    print(dim)


dimension(G, l_b_max + 1)
