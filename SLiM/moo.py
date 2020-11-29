import importlib
from datetime import datetime

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
from pymoo.model.problem import FunctionalProblem
from pymoo.visualization.scatter import Scatter
from pymoo.factory import get_performance_indicator

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

# cv = constraint violation
def save_front(z):
    time = datetime.now()
    file = open("results/resultsX_"+str(time)+".txt","w")
    for x in z:
        file.write("")
        file.write(str(x))
        file.write("\n")

def run_nsga():
    # Define range for decision variables
    range_pop = [0,100]
    range_selcoe = [0,1.0]
    algorithm = NSGA2(pop_size=100)
    termination = get_termination("n_gen",3)
    problem = FunctionalProblem(2,my_objs,xl=np.array([10,0]),xu=np.array([100,1]))
    result = minimize(problem,algorithm,termination,seed=1,save_history=True,verbose=True)
    """plot = Scatter()
    plot.add(result.F, color="red")
    plot.show()"""
    save_front(result.X)



print("Running NSGA")
run_nsga()