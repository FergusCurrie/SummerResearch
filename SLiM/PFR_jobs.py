# Script to call jobs for PFR
from moo import run_nsga
import pandas as pd
import os
import datetime

def sub_job():
    os.system("""
    INPUT=/workspace/hrafxc
    OUTPUT=0.1_raw_fastqc
    
    mkdir -p $OUTPUT
    module load  SLiM/3.1
    
    echo slim -d selectionstrength=0.8 seed 1 fish_simulation.slim | asub -j {$OUTPUT}/fastqc_analysis      
    
    """)

def make_all_jobs():
    # Makes system calls of a bunch of jobs
    path = "results/"+str(datetime.datetime.now()) + "_results"
    os.mkdir(path)
    for seed in open("seeds/algorithm_seed.txt"):
        seed = int(seed.strip())

        # Make a job



if True:
    make_all_jobs()
if True:
    sub_job()



