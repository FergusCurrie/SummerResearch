import importlib
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
from pymoo.model.problem import FunctionalProblem

import numpy as np

from slim import early_fitness, late_fitness


# maximize ?


objs = [
    lambda x: x[0]**2 + x[1]**2,
    lambda x: (x[0]-1)**2 + x[1]**2
]

my_objs = [
    lambda x: early_fitness(x),
    lambda x: late_fitness(x)

]

constr_ieq = [
    lambda x: 2*(x[0]-0.1) * (x[0]-0.9) / 0.18,
    lambda x: -20*(x[0]-0.4) * (x[0]-0.6) / 4.8
]


def run_nsga():
    # Define range for decision variables
    range_pop = [0,100]
    range_selcoe = [0,1.0]
    algorithm = NSGA2(pop_size=100)
    termination = get_termination("n_gen",40)
    #
    problem = FunctionalProblem(2,my_objs,xl=np.array([0,0]),xu=np.array([1,1]))


    result = minimize(problem,algorithm,termination,seed=1,save_history=True,verbose=True)


print("Running NSGA")
run_nsga()