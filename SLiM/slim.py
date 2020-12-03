import subprocess
from execution_time import ExecutionTime

from datetime import datetime

e = ExecutionTime()

def call_slim(population,select_coeff,ear,late,seed):
    """
    Sends decision variables to SLiM, early and late fitness returned in array

    :param dv (devision variables) , 0 -> pop, 1 -> sel_co
    :return: early fitness, late fitness
    """
    cmd = "slim -d selectionstrength=" + str(select_coeff) + " -d pop_size="+str(population)+" -d early="+str(ear)
    cmd += " -d late="+str(late) +" -seed "+str(seed)+" fish_simulation.slim"
    process = subprocess.run(cmd, shell=True, check=True, timeout=10,stdout=subprocess.PIPE)
    f = []
    for x in process.stdout.split():
        x = x.decode("utf-8")
        if "#" in x:
            f.append((x.replace("#","").replace('"',"")))
    return f

def call_slim_seed_average(population,select_coeff,ear,late):
    c = 0
    sum = [0,0]
    for x in open("seeds/slim_seed_train.txt","r"):
        c += 1
        g = call_slim(population=population,select_coeff=select_coeff,ear=ear,late=late,seed=int(x))
        sum[0] += float(g[0])
        sum[1] += float(g[1])
    sum[0] = sum[0] / c
    sum[1] = sum[1] / c
    return sum

def early_fitness(args) -> float:
    c = call_slim_seed_average(population=int(args[0]),select_coeff=float(args[1]),ear=100,late=4000)[0]
    return -1 * float(c)

def late_fitness(args) -> float:
    c= call_slim_seed_average(population=int(args[0]),select_coeff=float(args[1]),ear=100,late=4000)[1]
    return -1 * float(c)




