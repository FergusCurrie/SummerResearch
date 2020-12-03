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
    lambda x: early_fitness(x),
    lambda x: late_fitness(x)

]

# cv = constraint violation
def save_front(z):
    time = datetime.now()
    file = open("results/resultsX_"+str(time)+".txt","w")
    for x in z:
        file.write("")
        file.write(str(x))
        file.write("\n")
@e.timeit
def run_nsga():
    # Define range for decision variables
    range_pop = [0,100]
    range_selcoe = [0,1.0]
    algorithm = NSGA2(pop_size=30)
    termination = get_termination("n_gen",30)
    problem = FunctionalProblem(2,my_objs,xl=np.array([1,0]),xu=np.array([1000,1]))
    result = minimize(problem,algorithm,termination,seed=132,save_history=True,verbose=True)
    plot = Scatter()
    plot.add(result.F, color="red")
    plot.show()
    save_front(result.X)



print("Running NSGA")

run_nsga()
print(e.logtime_data)