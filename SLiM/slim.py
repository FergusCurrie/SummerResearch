import subprocess
from datetime import datetime

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

def bench_mark_slim(size):
    """
    HAving a look at execution times, dw about this
    :param size:
    :return:
    """
    start = datetime.now()
    for i in range(1,size):
        call_slim([size,0.5])
    stop = datetime.now()
    diff = stop - start
    print("Total seconds for "+ str(size)+ " executions: "+ str(diff.total_seconds()))
    print("AVG seconds per call for " + str(size) + " executions: " + str(diff.total_seconds()/size))


def early_fitness(args):
    return call_slim(population=int(args[0]*100+1),select_coeff=float(args[1]),ear=100,late=4000,seed=1)[0]

def late_fitness(args):
    return call_slim(population=int(args[0]*100+1),select_coeff=float(args[1]),ear=100,late=4000,seed=1)[1]



# Below is an example use of the call to slim, return value looks like : ['1.31454', '8.26002']
pop = 100
selc_coef = 0.1
early = 100
late = 4000
argsz=[100,0.3]
print(call_slim(population=argsz[0],select_coeff=argsz[1],ear=100,late=4000,seed=10))



