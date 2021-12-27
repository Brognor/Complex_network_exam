import time 
import RicciDiffusion as RD
import networkx as nx
import numpy as np
from tqdm import tqdm
import evolution as evo

f = open("datatime_formanfgfricci.txt","w")
for i in tqdm(range (2,503)):
    G=nx.complete_graph(i)
    
    vec=np.ones(i)
    vec=evo.normalize(vec)

    start=time.time()
    G=RD.preprocces_Forman(G)

    RD.FormanRicciEvolve_sign(G,vec,50)

    end=time.time()

    f.write(f"{i}\t{round((end-start),3)}\n")
    
f.close()
