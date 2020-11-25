import importlib
import pymoo as pym


algorithm = pym.NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling= pym.get_sampling("real_random"),
    crossover= pym.get_crossover("real_sbx", prob=0.9, eta=15),
    mutation= pym.get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)