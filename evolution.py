import networkx as nx
import networkit as nt
import numpy as np 
"""Small library to implement Laplacian evolution"""
def A(G):
    return nx.linalg.graphmatrix.adjacency_matrix(G) #A is initizalized as the adjacency matrix of the graph

def L(G):
    return nx.linalg.laplacianmatrix.laplacian_matrix(G) #L is initizalized as the lapalcian matrix of the graph

def D(G):
    return ( L(G)+ A(G) ) #D is the degree matrix

def transition_matrix(G):
    return (A(G)*np.linalg.inv(D(G)))

def evolution(G,vec,n_step):
    """This function realizes the diffusion of the vector vec on the graph for a number of step=n_step"""
    for i in range(n_step):
        vec=transition_matrix(G)*vec
    return vec
    


