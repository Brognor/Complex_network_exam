# RicciDiffusion.py
# diffusion considering also the curvature

# the quantity which must be difused is 
# represented as a vector 

import math
import importlib

# matplotlib setting
import matplotlib.pyplot as plt

# to print logs in jupyter notebook
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

# load GraphRicciCuravture package
from GraphRicciCurvature.OllivierRicci import OllivierRicci

# this does not care if the curvature is positive or negative

def RicciEvolve (G,vec,n_step):
   
    for t in range(n_step):
        W = [0] * len(list(G.nodes))
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
                W[n1] += abs(G[n1][n2]["ricciCurvature"])
    
        norm_vec = [0] * len(vec)
        vec_copy = vec
        for i in list(G.nodes):
            if W[i] != 0:
                norm_vec[i] = vec[i]/W[i]
    
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
                vec[n1] += abs(G[n1][n2]["ricciCurvature"]) * norm_vec[n2]
                vec[n2] -= abs(G[n1][n2]["ricciCurvature"]) * norm_vec[n2]
        
        check_parameter = abs( sum(vec)- sum(vec_copy) )/sum(vec)

        if check_parameter < 0.0001:
            vec = vec_copy
        else: 
            print("mass is not conserved, something happened")
            break

# this does

def RicciEvolve_sign (G,vec,n_step):
   
    for t in range(n_step):
        W = [0] * len(list(G.nodes))
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
               if(G[n1][n2]["ricciCurvature"]<0):
                  W[n1] += abs(G[n1][n2]["ricciCurvature"])
    
        norm_vec = [0] * len(vec)
        vec_copy = vec
        for i in list(G.nodes):
            if W[i] != 0:
                norm_vec[i] = vec[i]/W[i]
    
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
                if(G[n1][n2]["ricciCurvature"]<0):
                  vec[n1] += abs(G[n1][n2]["ricciCurvature"]) * norm_vec[n2]
                  vec[n2] -= abs(G[n1][n2]["ricciCurvature"]) * norm_vec[n2]
        
        check_parameter = abs( sum(vec)- sum(vec_copy) )/sum(vec)

        if check_parameter < 0.0001:
            vec = vec_copy
        else: 
            print("mass is not conserved, something happened")
            break
   return vec
           
         
 def Evolution_Flow(G, vec, n_step):
   for i in range(n_step):
        vec = RicciEvolve_sign(G, vec, 1)
        orc = OllivierRicci(G)
        orc.compute_ricci_flow(1)
        G = orc.G.copy()
