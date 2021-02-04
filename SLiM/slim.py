import subprocess

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
        cmd = "/software/bioinformatics/slim-3.1/slim -d selectionstrength=" + str(selection_coeff) + " -d lateSeed=" + str(seed).strip() + " fish_simulation.slim"
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


def early_fitness(args) -> float:
    c = call_slim(selection_coeff=float(args[0]))[0]
    return float(c)

def late_fitness(args) -> float:
    c= call_slim(selection_coeff=float(args[0]))[1]
    return float(c)


print(call_slim(0.8))

