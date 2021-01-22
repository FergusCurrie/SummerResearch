# Code to make a set of seeds for algorithm liek NSGA-2 and for slim

# First seeds made had z = 34604025023502 and zi = 344241

def make_sets():
    # Seed init and increment
    z = 346040 # Current seed
    zi = 344 # Seed increment
    num_seeds = 100

    # Seed slim training
    file = open("seeds/slim_seed_train.txt", "w")
    for x in range(0,num_seeds):
        file.write(str(z))
        z += zi
        file.write("\n")

    # Seed slim test
    file = open("seeds/slim_seed_test.txt", "w")
    for x in range(0, num_seeds):
        file.write(str(z))
        z += zi
        file.write("\n")

    # Seed algorithm
    file = open("seeds/algorithm_seed.txt", "w")
    for x in range(0, num_seeds):
        file.write(str(z))
        z += zi
        file.write("\n")





make_sets()
