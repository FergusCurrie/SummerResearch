import subprocess
from datetime import datetime

def call_slim(dv,timing):
    """
    Sends decision variables to SLiM, early and late fitness returned in array

    :param dv (devision variables) , 0 -> pop, 1 -> sel_co
    :return: early fitness, late fitness
    """
    cmd = "slim -d selectionstrength=" + str(dv[1]) + " -d pop_size="+str(dv[0])+" -d early="+str(timing[0])
    cmd += " -d late="+str(timing[1]) +" fish_simulation.slim"
    process = subprocess.run(cmd, shell=True, check=True, timeout=10,stdout=subprocess.PIPE)
    f = []
    for x in process.stdout.split():
        x = x.decode("utf-8")
        if "#" in x:
            f.append((x.replace("#","").replace('"',"")))
    return f

def save_output(a):
    """
    Saves a 2D array of results to file
    :param a: Takes list of decision vars with resulting objective functiosn
    :return: None
    """
    file = open("out.txt","w")
    file.write("pop , sel_co , obj1, obj2")
    file.write("\n")
    for x in a:
        for xx in x:
            file.write(str(xx))
            file.write(" ")
        file.write("\n")

def example_use():
    """
    Example use of call_sim and save_output, loops through a range
    Adjust domain to see change
    :return: none
    """
    # Set vars, results and domains of decision variables
    res = []
    domain_pop = [100,110]
    domain_sel_cof = [0.1,1.0,0.1]
    # Loops through permutations of decision variables, storing result in array
    for i in range(domain_pop[0],domain_pop[1]):
        j = domain_sel_cof[0]
        while j < domain_sel_cof[1]:
            early_fit, late_fit = call_slim([i, round(j, 1)],[100,4000])
            res.append([i, round(j, 1), early_fit, late_fit])
            j += domain_sel_cof[2]
    # Save to out.txt
    save_output(res)

def bench_mark_slim(size):
    start = datetime.now()
    for i in range(1,size):
        call_slim([size,0.5])
    stop = datetime.now()
    diff = stop - start
    print("Total seconds for "+ str(size)+ " executions: "+ str(diff.total_seconds()))
    print("AVG seconds per call for " + str(size) + " executions: " + str(diff.total_seconds()/size))

example_use()
#print(call_slim([100,0.1],[100,4000]))
#bench_mark_slim(100)
#example_use()