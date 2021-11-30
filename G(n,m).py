import matplotlib.pyplot as plt
import networkx as nx


#create and plot  a graph with n nodes and m edges

n = 10  # 10 nodes
m = 20  # 20 edges
seed = 20160  # seed random number generators for reproducibility

# Use seed for reproducibility
G = nx.gnm_random_graph(n, m, seed=seed)

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} {nx.clustering(G, v)}")
#coefficiente di clustering=N_collegamenti_fra_vicini/N_collegamenti_possibili_fra_vicini
print()


pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout, spring_layout per farlo posizionare in automatico
nx.draw(G, pos=pos) 
nx.draw_networkx(G, pos=pos, arrows=True, with_labels=True) #istanza di draw_networkx(G[, pos, arrows, with_labels]),disegna frecce direzionali e dà i nomi ai nodi




plt.show()


