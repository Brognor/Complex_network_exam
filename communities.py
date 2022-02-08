import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.operators.all import disjoint_union_all
from networkx.algorithms.operators.binary import disjoint_union
from random import randint
from GraphRicciCurvature.OllivierRicci import OllivierRicci

colors=['r','b','g','c','m','y','darkorange','lime','rebeccapurple','hotpink','slategrey']

classic_communities=girvan_newman

def ricci_communities(G,iterations=20):
    orc_G = OllivierRicci(G,verbose='INFO')
    orc_G.compute_ricci_flow(iterations)
    return orc_G.ricci_community()


def plot_classic_communities(G,community_list): #input is an array of arrays containing node number of each community of G

    node_groups = []
    for com in next(community_list):
        node_groups.append(list(com)) 
        

    colormap=[]
    for  node in G:
        for i in range(len(node_groups)):
            if node in node_groups[i]:
                colormap.append(colors[i])

    fig=plt.figure()
    nx.draw_networkx(G, node_color=colormap, with_labels=True,pos=nx.spring_layout(G))

    

    fig.savefig('communities.png')




def plot_ricci_communities(G,dictionary): #dictionary is the cmmunity dictionary given by ricci_communities    
    N = len(G.nodes)
    nodes_community = [0]*N  
    node_colors =  [0]*N 
    for key, value in dictionary[1].items():
            nodes_community[key]=value
            node_colors[key]=colors[value]
    fig=plt.figure()
    nx.draw_networkx(G,node_color =node_colors, with_labels=True,pos=nx.spring_layout(G))

    fig.savefig('communities_ricci.png')
    



"""
test program
G=nx.karate_club_graph()
com=classic_communities(G)

plot_classic_communities(G,com)

G=nx.karate_club_graph()
com_1=ricci_communities(G)
plot_ricci_communities(G,com_1)
"""



