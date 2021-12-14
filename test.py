import evolution.py


G = nx.gnm_random_graph(60,120)
vec=[i for i in range(0,60)]
L=evolution_collection(G,vec,12)
plot_all_evolution(G,L,node_dimension=400)
