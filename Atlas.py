
import matplotlib.pyplot as plt
import networkx as nx
#BARABASI ALBERT GRAPH
n = 20  # 20 nodes
m =  2 # 2 edges for each added
seed = 20160  # seed random number generators for reproducibility

# Use seed for reproducibility
G = nx.barabasi_albert_graph(n, m, seed=None, initial_graph=G)#istanza di barabasi_albert_graph(n, m, seed=None, initial_graph=None) 
#nelle vecchie versione di networkx non va initial_graph
# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} {nx.clustering(G_1, v)}")
#coefficiente di clustering=N_collegamenti_fra_vicini/N_collegamenti_possibili_fra_vicini
print()


pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout

nx.draw(G, pos=pos)
nx.draw_networkx(G, pos=pos, arrows=True, with_labels=True)
plt.show()

n = 10  # 10 nodes
p = 0.2  # 20 edges
seed = 20160  # seed random number generators for reproducibility
#BINOMIAL GRAPH
# Use seed for reproducibility
G = nx.binomial_graph(n, p, seed=seed)#istanza di binomial_graph(n, p, seed=None, directed=False)
#binomial_graph() and erdos_renyi_graph() are aliases for gnp_random_graph()

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} {nx.clustering(G, v)}")
#coefficiente di clustering=N_collegamenti_fra_vicini/N_collegamenti_possibili_fra_vicini
print()


pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout

nx.draw(G, pos=pos)
nx.draw_networkx(G, pos=pos, arrows=True, with_labels=True)
plt.show()
