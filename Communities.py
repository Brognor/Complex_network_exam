import scipy.linalg as linalg
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def Communities(G):
    Laplacian = nx.linalg.laplacianmatrix.laplacian_matrix(G)
    w, v = linalg.eig(Laplacian)
    w = w.real
    u = w
    u.sort()
    lam = np.where(w == u[1])

    com_1 = []
    com_2 = []
    color_map = []

    for i in range(len(G.nodes)):
        if v[i][lam[0]] > 0:
            com_1 = np.append(com_1, i)
            color_map = np.append(color_map, "blue")
        else:
            com_2 = np.append(com_2, i)
            color_map = np.append(color_map, "red")
    return com_1, com_2, color_map
