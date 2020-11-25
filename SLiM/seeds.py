# Code to make a set of seeds for algorithm liek NSGA-2 and for slim

# First seeds made had z = 34604025023502 and zi = 344241

def make_sets():
    # Seed init and increment
    z = 34604025023502 # Current seed
    zi = 344241 # Seed increment

    # Seed slim training
    file = open("slim_seed_train.txt", "w")
    for x in range(0,100):
        file.write(str(z))
        z += zi
        file.write("\n")

    # Seed slim test
    file = open("slim_seed_test.txt", "w")
    for x in range(0, 100):
        file.write(str(z))
        z += zi
        file.write("\n")

    # Seed algorithm
    file = open("algorithm_seed.txt", "w")
    for x in range(0, 100):
        file.write(str(z))
        z += zi
        file.write("\n")

make_sets()










make_sets()