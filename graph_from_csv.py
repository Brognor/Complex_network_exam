import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Data = open("musae_git_edges.csv", "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.Graph()

G = nx.parse_edgelist(
    Data, delimiter=",", create_using=Graphtype, nodetype=int, data=(("weight", float),)
)

nx.draw(G)
plt.show()
