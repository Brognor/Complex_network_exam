# RicciDiffusion.py
# diffusion considering also the curvature

# the quantity which must be difused is 
# represented as a vector 

import math
import importlib
import time
# matplotlib setting
import matplotlib.pyplot as plt

# to print logs in jupyter notebook
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

# load GraphRicciCuravture package
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.FormanRicci import FormanRicci

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

def OllivierRicciEvolve_sign (G,vec,n_step):
   
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

        vec = vec_copy

    return vec

def FormanRicciEvolve_sign (G,vec,n_step):
   
    for t in range(n_step):
        W = [0] * len(list(G.nodes))
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
               if(G[n1][n2]["formanCurvature"]<0):
                  W[n1] += abs(G[n1][n2]["formanCurvature"])
    
        norm_vec = [0] * len(vec)
        vec_copy = vec
        for i in list(G.nodes):
            if W[i] != 0:
                norm_vec[i] = vec[i]/W[i]
    
        for n1 in list(G.nodes):
            for n2 in list(G.neighbors(n1)):
                if(G[n1][n2]["formanCurvature"]<0):
                  vec[n1] += abs(G[n1][n2]["formanCurvature"]) * norm_vec[n2]
                  vec[n2] -= abs(G[n1][n2]["formanCurvature"]) * norm_vec[n2]

        vec = vec_copy

    return vec           
         
def OllivierEvolution_Flow(G, vec, n_step):
    for i in range(n_step):
        vec = OllivierRicciEvolve_sign(G, vec, 1)
        orc = OllivierRicci(G)
        orc.compute_ricci_flow(1)
        G = orc.G.copy()

def FormanEvolution_Flow(G, vec, n_step):
    for i in range(n_step):
        vec = FormanRicciEvolve_sign(G, vec, 1)
        orc = FormanRicci(G)
        orc.compute_ricci_flow(1)
        G = orc.G.copy()

def preprocces_Ollivier(G):

    orf= OllivierRicci(G)
    orf.compute_ricci_curvature()
    return orf.G.copy()
    
def preprocces_Forman(G):

    orf= FormanRicci(G)
    orf.compute_ricci_curvature()
    return orf.G.copy()
