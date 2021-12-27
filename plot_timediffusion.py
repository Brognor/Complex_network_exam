import matplotlib.pyplot as plt

figu=plt.figure()
ax= figu.add_subplot(111)
ax.set_title("Execution time comparison")
ax.set_xlabel("Number of nodes")
ax.set_ylabel("Time (s)")

with open("datatime_diff.txt","r") as f:
    lines=f.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
    fig=plt.figure()
    ax1= fig.add_subplot(111)

    ax1.set_title("Execution time T matrix")
    ax1.set_xlabel("Number of nodes")
    ax1.set_ylabel("Time (s)")
    ax1.plot(x,y,c='r', linewidth=1,label='Diffusion with T matrix')
    
    ax.plot(x,y,c='r', linewidth=1,label='Diffusion with T matrix')
    plt.legend()

    fig.savefig("transition_time.png",dpi=150)

    f.close()

with open("datatime_ollivierricci.txt","r") as f:
    lines=f.readlines()
    x=[float(line.split()[0]) for line in lines]
    y=[float(line.split()[1]) for line in lines]
    fig=plt.figure()
    ax1= fig.add_subplot(111)

    ax1.set_title("Execution time OllivierRicci")
    ax1.set_xlabel("Number of nodes")
    ax1.set_ylabel("Time (s)")
    ax1.plot(x,y,c='g', linewidth=1,label='Diffusion with OllivierRicci')

    ax.plot(x,y,c='g', linewidth=1,label='Diffusion with OllivierRicci')
    plt.legend()

    fig.savefig("ollivierricci_time.png",dpi=150)

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
    ax1.plot(x,y,c='b', linewidth=1,label='Diffusion with FormanRicci')

    ax.plot(x,y,c='b', linewidth=1,label='Diffusion with FormanRicci')
    plt.legend()

    fig.savefig("formanricci_time.png",dpi=150)

    f.close()
ax.legend()
figu.savefig("Comparison.png",dpi=150)
ax.set_xlim(0,60)
ax.set_ylim(0,1)
figu.savefig("Comparison_low.png",dpi=150)
