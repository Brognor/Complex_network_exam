import time 
import RicciDiffusion as RD
import networkx as nx
import numpy as np
from tqdm import tqdm
import evolution as evo

f = open("datatime_classic.txt","w")
for i in tqdm(range (2,500)):
    G=nx.complete_graph(i)
    
    vec=np.ones(i)
    vec=evo.normalize(vec)

    start=time.time()
    

    evo.evolution(G,vec,10)

    end=time.time()

    f.write(f"{i}\t{round((end-start),5)}\n")
    
f.close()


f = open("datatime_ollivierricci.txt","w")
for i in tqdm(range (2,250)):
    G=nx.complete_graph(i)
    
    vec=np.ones(i)
    vec=evo.normalize(vec)

    start=time.time()
    G=RD.preprocces_Ollivier(G)

    RD.OllivierRicciEvolve_sign(G,vec,10)

    end=time.time()

    f.write(f"{i}\t{round((end-start),3)}\n")
    
f.close()



f = open("datatime_formanricci.txt","w")
for i in tqdm(range (2,500)):
    G=nx.complete_graph(i)
    
    vec=np.ones(i)
    vec=evo.normalize(vec)

    start=time.time()
    G=RD.preprocces_Forman(G)

    RD.FormanRicciEvolve_sign(G,vec,10)

    end=time.time()

    f.write(f"{i}\t{round((end-start),4)}\n")
    
f.close()
