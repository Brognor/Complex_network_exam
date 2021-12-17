import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import imageio
import scipy.sparse as sp 
import os

"""Small library to implement Laplacian evolution"""


def normalize(v): #Normalize the vector given as input
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm


def A(G):
    return nx.linalg.graphmatrix.adjacency_matrix(G) #A is initizalized as the adjacency matrix of the graph

def L(G):
    return nx.linalg.laplacianmatrix.laplacian_matrix(G) #L is initizalized as the lapalcian matrix of the graph

def D(G):
    return ( L(G)+ A(G) ) #D is the degree matrix

def transition_matrix(G):
    if nx.is_connected(G):
        return (A(G)*(np.linalg.inv(D(G).toarray())))
    else: 
        A_mod=sp.csr_matrix.toarray(A(G))
        D_mod=sp.csr_matrix.toarray(D(G))
        for i in list(nx.isolates(G)):
            A_mod[i][i]+=1
            D_mod[i][i]+=1
        A_mod=sp.csr_matrix(A_mod)
        D_mod=sp.csr_matrix(D_mod)

        return (A_mod*(np.linalg.inv(D_mod.toarray())))





    #####################################à

def evolution(G,vec,n_step,norm=True):
    """This function realizes the diffusion of the vector vec on the graph for a number of step=n_step, 
    if norm is true it normalize the input vector"""
    if norm:
        vec=normalize(vec)
    for i in range(n_step):
        vec=transition_matrix(G).dot(vec)
    return vec

########################


def evolution_collection(G,vec,n_step,norm=True):
    """This function realizes the diffusion of the vector vec on the graph for a number of step=n_step and return 
    an array with all the intermediate graphs"""

    graph_array=np.empty((n_step+1,len(vec)))
    if norm:
        vec=normalize(vec)
    graph_array[0]=vec
    for i in range(n_step):
        vec=transition_matrix(G).dot(vec)
        graph_array[i+1]=vec
    return graph_array


#############################à

def plot_evolution(G,vec,norm=True,lenght=15,height=15,node_dimension=300,K=0.5):
    if norm:
        vec=normalize(vec)
    plt.figure(figsize=(lenght,height)) 
    layout=nx.spring_layout(G,k=K)
    nx.draw_networkx(G,pos=layout,labels={n: np.around(vec,2)[n] for n in G},node_color=vec,cmap=plt.cm.Reds,node_size=node_dimension)


    #######################################

def plot_all_evolution(G,vec_collection,norm=True,saveall=False,lenght=15,height=15,pause=1,node_dimension=300,K=0.5):

    """Take an array of vector and a graph, each element of the vector represent the label of the node and create a gif.
    The i-th image of the gif is the graph with the label in the i-th vector of the array"""
    if norm:
        for i in range(len(vec_collection)):
            normalize(vec_collection[i])
    
    filenames=[]
    numerfig=1

    layout=nx.spring_layout(G,k=K) #needed to avoid different spring in each figure

    for vec in vec_collection:

        plt.figure(figsize=(lenght,height))  #adjustable lenght and height
        nx.draw_networkx(G,pos=layout,labels={n: np.around(vec,2)[n] for n in G},node_color=vec,cmap=plt.cm.Reds,node_size=node_dimension)
        filename = f'{numerfig}.png'
        filenames.append(filename)

        
       
        plt.title('step%s' %numerfig)
        plt.savefig(filename)
        plt.clf()
        numerfig=numerfig+1
        plt.close() #useful to avoid memory problems

    images=[]

    for filename in filenames:
        images.append(imageio.imread(filename))
        
    imageio.mimsave('./evolution.gif', images,duration=pause)

    if not saveall: #if saveall is as given we cancel all the intermediate images mantaining only the gif
        for filename in set(filenames):
            os.remove(filename)


    ####################################




