import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True #allow using tex in legend

def quadratic(x,a,b,c):
    return a*np.power(x,2)+np.multiply(b,x)+c

def cubic(x,a,b,c,d):
    return a*np.power(x,3)+b*np.power(x,2)+np.multiply(c,x)+d

def quartic(x,a,b,c,d,e):
    return a*np.power(x,3)+b*np.power(x,3)+c*np.power(x,2)+np.multiply(d,x)+e

def expo(x,a,b,c,d):
    return a*np.exp(np.multiply(b,x))+np.multiply(c,x)+d


with open("datatime_diff.txt","r") as f:
    lines=f.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
    fig=plt.figure()
    ax1= fig.add_subplot(111)

    ax1.set_title("Execution time T matrix")
    ax1.set_xlabel("Number of nodes")
    ax1.set_ylabel("Time (s)")
    ax1.plot(x,y, linewidth=1,label='Diffusion with T matrix')
    
    par,cov=opt.curve_fit(quadratic,x,y,bounds=(0,np.inf))

    y_1 = quadratic(x,par[0],par[1],par[2])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],5)}$n^2+${round(par[1],16)}$n+${round(par[2],16)}')
    plt.legend()

    fig.savefig("fit_transition_time.png",dpi=150)

    f.close()

with open("datatime_formanricci.txt","r") as f:
    lines=f.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
    fig=plt.figure()
    ax1= fig.add_subplot(111)

    ax1.set_title("Execution time FormanRicci")
    ax1.set_xlabel("Number of nodes")
    ax1.set_ylabel("Time (s)")
    ax1.plot(x,y, linewidth=1,label='FormanRicci')
    
    par,cov=opt.curve_fit(quadratic,x,y,bounds=(0,np.inf))

    y_1 = quadratic(x,par[0],par[1],par[2])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],5)}$n^2+${round(par[1],26)}$n+${round(par[2],26)}')
    plt.legend()

    fig.savefig("fit_FormanRicci_time.png",dpi=150)

with open("datatime_ollivierricci.txt","r") as f:
    lines=f.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
    fig=plt.figure()
    ax1= fig.add_subplot(111)

    ax1.set_title("Execution time OllivierRicci")
    ax1.set_xlabel("Number of nodes")
    ax1.set_ylabel("Time (s)")
    ax1.plot(x,y,linewidth=1,label='OllivierRicci')
    
    par,cov=opt.curve_fit(quadratic,x,y,bounds=(0,np.inf))
    y_1 = quadratic(x,par[0],par[1],par[2])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],5)}$n^2+${round(par[1],23)}$n+${round(par[2],24)}')

    par,cov=opt.curve_fit(cubic,x,y,bounds=(0,np.inf))
    y_1 = cubic(x,par[0],par[1],par[2],par[3])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],5)}$n^3+${round(par[1],24)}$n^2+${round(par[2],24)}$n+${round(par[3],24)}')

    par,cov=opt.curve_fit(quartic,x,y,bounds=(0,np.inf))
    y_1 = quartic(x,par[0],par[1],par[2],par[3],par[4])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],9)}$n^4+${round(par[1],5)}$n^3+${round(par[2],10)}$n^2+${round(par[3],10)}$n+${round(par[4],10)}')
    
    par,cov=opt.curve_fit(expo,x,y,p0=(3,0.02,0,0),bounds=(0,np.inf))
    y_1=expo(x,par[0],par[1],par[2],par[3])
    ax1.plot(x,y_1,linewidth=1,label=f'fit : {round(par[0],2)}$\exp$({round(par[1],3)}n)+{round(par[2],12)}$n+${round(par[3],23)}')
    
    plt.legend()
 

    fig.savefig("fit_OllivierRicci_time.png",dpi=150)

