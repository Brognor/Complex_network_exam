import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt



G_4=nx.tetrahedral_graph() #tetraedro
nx.draw_networkx(G_4, node_size=300)
plt.show()

G_4T=nx.truncated_tetrahedron_graph() #tetraedro troncato
nx.draw_networkx(G_4T, node_size=300)
plt.show()


G_6=nx.cubical_graph() #cubo
nx.draw_networkx(G_6)
plt.show()

G_8=nx.octahedral_graph() #cubo
nx.draw_networkx(G_8)
plt.show()

G_12=nx.dodecahedral_graph() #dodecaedro
nx.draw_networkx(G_12)
plt.show()


G_20=nx.icosahedral_graph() #icosaaedro
nx.draw_networkx(G_20, node_size=300)
plt.show()


F=nx.compose(G_6,G_8)#Composition is the simple union of the node sets and edge sets. The node sets of G and H do not need to be disjoint.
#If nodes have same names this can be used to link graph together.
nx.draw_networkx(F)
plt.show()

F=nx.disjoint_union(G_6,G_8)
nx.draw_networkx(F)
plt.show()
"""Return the union of graphs G and H.

Graphs G and H must be disjoint, otherwise an exception is raised. If we use the functon union."""
F.add_edge(7,8)
nx.draw_networkx(F)
plt.show()
"""We have linked the graph together"""
