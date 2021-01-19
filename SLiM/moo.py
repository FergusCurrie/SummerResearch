import importlib
from datetime import datetime

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
from pymoo.model.problem import FunctionalProblem
from pymoo.visualization.scatter import Scatter
from pymoo.factory import get_performance_indicator
from execution_time import ExecutionTime
import numpy as np

from slim import early_fitness, late_fitness


# maximize ?

e = ExecutionTime()

my_objs = [
    lambda x: -early_fitness(x),
    lambda x: -late_fitness(x)
]

# cv = constraint violation
def save_front(z,zz,s):
    time = datetime.now()
    file = open("results/"+(str(s).strip())+"_results.txt","w")
    for x in z:
        file.write("")
        file.write(str(x[0]))
        file.write(",")
        file.write(str(x[1]))
        file.write("\n")
    file.write("#")
    file.write("\n")

    for x in zz:
        file.write("")
        file.write(str(x[0]))
        file.write(",")
        file.write(str(x[1]))
        file.write("\n")

@e.timeit
def run_nsga(s):
    # Define range for decision variables
    algorithm = NSGA2(pop_size=50)
    termination = get_termination("n_gen",40)
    problem = FunctionalProblem(1,my_objs,xl=np.array([0]),xu=np.array([1]))
    result = minimize(problem,algorithm,termination,seed=int(s),save_history=True,verbose=True)
    save_front(result.F,result.X,s)
