import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import imageio
import scipy.sparse as sp 
import os

"""Small library to implement Laplacian evolution"""


def normalize(v): #Normalize the vector given as input with the 1-norm
    v=np.array(v)
    return v/sum(v)



def A(G):
    A=nx.adjacency_matrix(G) #A is initizalized as the adjacency matrix of the graph
    return sp.csr_matrix.toarray(A)

def L(G):
    L=nx.laplacian_matrix(G) #L is initizalized as the lapalcian matrix of the graph
    return sp.csr_matrix.toarray(L)

def D(G):
    return ( L(G)+ A(G) )#D is the degree matrix

def L_t(G):
    return (D(G)-A(G))*(np.linalg.inv(D(G)))


def transition_matrix(G):
    if nx.is_connected(G):
        return np.matmul(A(G),np.linalg.inv(D(G)))
    else: 
        
        A_mod=A(G)
        D_mod=D(G)
        for i in list(nx.isolates(G)):
            A_mod[i][i]+=1
            D_mod[i][i]+=1

        return np.matmul(A_mod,np.linalg.inv(D_mod))





    #####################################à

def evolution(G,vec,n_step,norm=True):
    """This function realizes the diffusion of the vector vec on the graph for a number of step=n_step, 
    if norm is true it normalize the input vector"""
    if norm:
        vec=normalize(vec)
    T=transition_matrix(G)
    

    for i in range(n_step):
        vec=np.dot(T,vec)
        
   
    return vec

########################


def evolution_collection(G,vec,n_step,norm=True):
    """This function realizes the diffusion of the vector vec on the graph for a number of step=n_step and return 
    an array with all the intermediate graphs"""

    graph_array=np.empty((n_step+1,len(vec)))
    if norm:
        vec=normalize(vec)
    graph_array[0]=vec
    T=transition_matrix(G)

    for i in range(n_step):
        vec=np.dot(T,vec)
        graph_array[i+1]=vec
    return graph_array


#############################à

def plot_evolution(G,vec,norm=True,lenght=15,height=15,node_dimension=300,layout=nx.spring_layout,label=True):
    if norm:
        vec=normalize(vec)
    plt.figure(figsize=(lenght,height)) 
    layout=layout
    nx.draw_networkx(G,pos=layout,labels={n: np.around(vec,2)[n] for n in G},node_color=vec,cmap=plt.cm.Reds,node_size=node_dimension,with_labels=label)
    Norm=mpl.colors.Normalize(min(vec),max(vec))
    plt.colorbar(plt.cm.ScalarMappable(norm=Norm,cmap=plt.cm.Reds))
    


    #######################################

def plot_all_evolution(G,vec_collection,norm=True,saveall=False,lenght=15,height=15,pause=1,node_dimension=300,label=True,layout=nx.spring_layout):

    """Take an array of vector and a graph, each element of the vector represent the label of the node and create a gif.
    The i-th image of the gif is the graph with the label in the i-th vector of the array"""
    if norm:
        for i in range(len(vec_collection)):
            normalize(vec_collection[i])
    
    filenames=[]
    numerfig=1

    layout=layout #needed to avoid different spring in each figure

    for vec in vec_collection:

        plt.figure(figsize=(lenght,height))  #adjustable lenght and height
        nx.draw_networkx(G,pos=layout,labels={n: np.around(vec,2)[n] for n in G},node_color=vec,cmap=plt.cm.Reds,vmin=min(vec), vmax=max(vec),node_size=node_dimension,with_labels=label)
        filename = f'{numerfig}.png'
        filenames.append(filename)
        Norm=mpl.colors.Normalize(min(vec),max(vec))

        
       
        plt.title('step%s' %numerfig)
        plt.colorbar(plt.cm.ScalarMappable(norm=Norm,cmap=plt.cm.Reds))
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









    


