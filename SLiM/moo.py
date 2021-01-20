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
import pandas as pd

from slim import early_fitness, late_fitness


# maximize ?

e = ExecutionTime()

my_objs = [
    lambda x: -early_fitness(x),
    lambda x: -late_fitness(x)
]


@e.timeit
def run_nsga(s):
    # Define range for decision variables
    algorithm = NSGA2(pop_size=50)
    termination = get_termination("n_gen",40)
    problem = FunctionalProblem(1,my_objs,xl=np.array([0]),xu=np.array([1]))
    result = minimize(problem,algorithm,termination,seed=int(s),save_history=True,verbose=True)
    return result.F,result.X

def make_job(seed):
    resX, resF = run_nsga(seed)
    results_list = []
    for i in range(0, len(resX)):
        results_list.append([resX[i], resF[i][0], resF[i][1]])
    df = pd.DataFrame(results_list, columns=["Selection Coefficient", "Early Fitness", "Late Fitness"])