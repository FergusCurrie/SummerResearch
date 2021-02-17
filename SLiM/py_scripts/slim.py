import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime


def call_slim(selection_coeff):
    """
    Sends decision variables to SLiM, early and late fitness returned in array

    :param dv (devision variables) , 0 -> pop, 1 -> sel_co
    :return: early fitness, late fitness
    """
    c = 0
    sum = [0, 0]
    for seed in open("seeds/slim_seed_train.txt", "r"):
        c += 1
        cmd = "/software/bioinformatics/slim-3.1/slim -d selectionstrength=" + str(selection_coeff) + " -d lateSeed=" + str(seed).strip() + " ../slim_scripts/fish_simulation.slim"
        #cmd = "slim -d selectionstrength=" + str(selection_coeff) +" -d lateSeed="+str(seed).strip()+" fish_simulation.slim"
        process = subprocess.run(cmd, shell=True, check=True, timeout=10,stdout=subprocess.PIPE)
        f = []
        for x in process.stdout.split():
            x = x.decode("utf-8")
            if "#" in x:
                f.append((x.replace("#","").replace('"',"")))
        sum[0] += float(f[0])
        sum[1] += float(f[1])
    sum[0] = sum[0] / c
    sum[1] = sum[1] / c
    return sum

def fitness_vs_generation(selection_coeff):

    c = 0
    res = []
    for seed in open("../data/seeds/slim_seed_train.txt", "r"):
        if c > 30:
            break
        cmd = "slim -d selectionstrength=" + str(selection_coeff) + " -d lateSeed=" + str(seed).strip() + " ../slim_scripts/graph_fitness_generation.slim"
        #print(cmd)
        process = subprocess.run(cmd, shell=True, check=True, timeout=10,stdout=subprocess.PIPE)
        f = []
        for x in process.stdout.split():
            x = x.decode("utf-8")
            if "#" in x:
                f.append((x.replace("#","").replace('"',"")))
        for i in range(0, len(f)):
            #print(f[i])
            try:
                if c == 0:
                    res.append(float(f[i]))
                else:
                    res[i] += float(f[i])
            except:
                continue
        c += 1

    # Average

    for i in range(0,len(res)):
        res[i] = [res[i] / c,i]


    return pd.DataFrame(data=np.array(res),columns=["Fitness","Generations"])

def mutation_vs_generation(selection_coeff):
    return
    '''c = 0
    res = []
    for si,seed in enumerate(open("seeds/slim_seed_train.txt", "r")):
        c += 1
        #cmd = "/software/bioinformatics/slim-3.1/slim -d selectionstrength=" + str(selection_coeff) + " -d lateSeed=" + str(seed).strip() + " fish_simulation.slim"
        #cmd = "slim -d selectionstrength=" + str(selection_coeff) +" -d lateSeed="+str(seed).strip()+" test.slim"
        process = subprocess.run(cmd, shell=True, check=True, timeout=10,stdout=subprocess.PIPE)
        f = []
        for x in process.stdout.split():
            x = x.decode("utf-8")
            if "#" in x:
                f.append((x.replace("#","").replace('"',"")))
        for i in range(0,len(f)):
            if si == 0:
                res.append(float(f[i]))
            else:
                res[i] += float(f[i])

    # Average

    for i in range(0,len(f)):
        res[i] = res[i] / c

    print(res)
    #return pd.DataFrame(data=np.array(sum),columns=["Fitness","Generations"])'''



def early_fitness(args) -> float:
    c = call_slim(selection_coeff=float(args[0]))[0]
    return float(c)

def late_fitness(args) -> float:
    c= call_slim(selection_coeff=float(args[0]))[1]
    return float(c)


'''df = call_slim_graphing(0.4)
df.plot.scatter(x="Generations", y="Fitness", s=5, title="Test")
df1 = call_slim_graphing(0.9)
df1.plot.scatter(x="Generations", y="Fitness", s=5, title="Test")
plt.show(block=True)'''

#0.99999955

# Graphing fitness over time
if False:
    z = []
    f = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    ss = [0.8,0.9]
    for x in ss:
        #print(x)
        z.append(fitness_vs_generation(x))

    fig = plt.figure()
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    for i,frame in enumerate(z):
        plt.plot(frame['Generations'],frame['Fitness'],label=str(ss[i]))
    plt.legend()
    plt.show(block=True)

# Graphing mutation count.
if False:
    mutation_vs_generation(0.9)

# Graphing start


