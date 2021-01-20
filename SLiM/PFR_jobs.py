# Script to call jobs for PFR
from moo import run_nsga
import pandas as pd
import os
import datetime

def sub_job():
    os.system("""
    INPUT=/workspace/hrafxc

    OUTPUT="results_test"
    
    mkdir -p $OUTPUT
   
          
    
    for x in {1..1}
    do 
	bsub -o ${OUTPUT}/${x}.out /software/bioinformatics/slim-3.1/slim -d selectionstrength=0.8 -seed $x fish_simulation.slim;
    done 
	
    """)

def make_all_jobs():
    # Makes system calls of a bunch of jobs
    path = "results/"+str(datetime.datetime.now()) + "_results"
    os.mkdir(path)
    for seed in open("seeds/algorithm_seed.txt"):
        seed = int(seed.strip())

        # Make a job



if False:
    make_all_jobs()
if True:
    sub_job()



