# Script to call jobs for PFR
from moo import run_nsga
import pandas as pd
import os
import datetime



def sub_job(seed):
    os.system("""
    INPUT=/workspace/hrafxc

    OUTPUT="results_test"
    
    mkdir -p $OUTPUT
   
    bsub -o {v2} python3 moo.py {v1}; 
	
    """.format(
        v1 = seed,
        v2 = "${OUTPUT}/"+str(seed)+".out"
    ))

def make_all_jobs():
    # Makes system calls of a bunch of jobs
    path = "results/"+str(datetime.datetime.now()) + "_results"
    #os.mkdir(path)
    for seed in open("seeds/algorithm_seed.txt"):
        seed = int(seed.strip())
        sub_job(seed)
        # Make a job


if True:
    make_all_jobs()
if False:
    sub_job(323)



