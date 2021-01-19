import sys
import datetime
from moo import run_nsga
from pymoo.visualization.scatter import Scatter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def makejobs():
    """
    Makes a job list in file joblist.txt
    """
    print("Making jobs list in joblist.txt")

def executejobs():
    """
    While loop that executes all jobs in job list
    """
    print("Executing nsga2 for each seed")
    # Find num jobs
    nsga_seeds = []
    for line in open("seeds/algorithm_seed.txt","r"):
        nsga_seeds.append(line)

    # Execute jobs
    for x in nsga_seeds:
        run_nsga(x)

def old_graph(s):
    """
    This code is horrific. Unfortunately started local NSGA2 without checking so will have to do for now
    :param s: seed
    :return: nothing
    """
    data = []
    for x in open("results/"+str(s)+"_results.txt"):
        if "    " in x:
            x = x.replace("    ",",")
        if "   " in x:
            x = x.replace("   ",",")
        if "  " in x:
            x = x.replace("  ",",")
        if " " in x:
            x = x.replace(" ",",")
        x = x.replace("[","").replace("]","").replace("\n","")
        x = x.strip()
        x = x.split(",")
        # remove empty
        z = []
        for xx in x:
            if xx != '':
                z.append(xx)
        if z != []:
            data.append([float(z[0]),float(z[1])])
    Scatter().add(np.array(data)).show()

def graph(s):
    """
    This code is horrific. Unfortunately started local NSGA2 without checking so will have to do for now
    :param s: seed
    :return: nothing
    """
    data = []
    input = []
    datat = True
    mixed = [[],[],[],[]]
    for x in open("results/"+str(s)+"_results.txt"):
        x = x.replace("\n","")
        if x == "#":
            datat = False
            continue
        x = x.replace("\n","")
        x = x.split(",")
        if datat:
            data.append([-float(x[0]),-float(x[1])])
            mixed[0].append(-float(x[0]))
            mixed[1].append(-float(x[1]))
        else:
            input.append([int(float(x[0])), float(x[1])])
            mixed[2].append(int(float(x[0])))
            mixed[3].append(float(x[1]))
    #Scatter(tight_layout=True).add(np.array(mixed),s=10).show()
    #Scatter().add(np.array(data)).show()
    #Scatter().add(np.array(input)).show()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.array(mixed[0])
    y = np.array(mixed[1])
    z = np.array(mixed[2])
    c = np.array(mixed[3])

    img = ax.scatter(x, y, z, c=c, cmap=plt.cool())
    fig.colorbar(img)
    plt.show()

def com_result(s):
    hash = -1
    l = []
    res = []
    for x in open("results/"+str(s)+"_results.txt"):
        l.append(x)
    for i in range(0,len(l))    :
        x = l[i]
        if hash == -1:
            if "#" in x:
                hash = i
            continue
        else:
            res.append((l[i-hash-1]+","+l[i]).replace("\n",""))
    for x in res:
        x = x.split(",")
        aa = str(round(float(x[0])*-1,2))
        bb = str(round(float(x[1])*-1,2))
        cc = str(int(float(x[2])))
        dd = str(round(float(x[3]),2))
        print(aa+","+bb+","+cc+","+dd)

"""
Call method based on args 
Usage : 
    m = make jobs 
    e = execute jobs 
"""
if((sys.argv)[1] == "m"):
    makejobs()
if((sys.argv)[1] == "e"):
    executejobs()
if((sys.argv)[1] == "g"):
    graph(sys.argv[2])
if((sys.argv)[1] == "c"):
    com_result(sys.argv[2])