import numpy as np
import networkx as nx
from random import randint





def Color_graph(G,dictionary):
    N = len(G.nodes)
    color = []
    node_color = [0] * N
    for i in range(N):
        color.append("#%06X" % randint(0, 0xFFFFFF))
      
    for key, value in dictionary.items():
        node_color[key] = color[value]
    return node_color
