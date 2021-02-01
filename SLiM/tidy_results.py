
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def clean():
    """
    Dirty method for cleaning results... Makes csv files with pandas dataframes of x,obj1,obj2
    :return:
    """
    fn = "results_test"
    for x in os.listdir(fn):
        found = "None"
        res = ""
        resx = ""
        # Get basic function chunk
        for y in open(fn+"/"+x,'r'):
            #print(y)
            if "function:" in y:
                found = "y"
            if found == "y":
                if "x:" in y:
                    found = "x"
                else:
                    res += y
            if found == "x":
                if "-------" in y:
                    found = "None"
                else:
                    resx += y

        res = res.replace("\n","").replace("function:","").replace("x:","").replace("[","#").replace("]","#")
        fs = []
        for e in res.split("#"):
            es = e.split(" ")
            es = [xi for xi in es if xi != '']
            if es == []:
                continue
            if is_number(es[0]):
                fs.append(es)

        resx = resx.replace("\n", "").replace("function:", "").replace("x:", "").replace("[", "#").replace("]", "#")
        xs = []
        for e in resx.split("#"):
            es = e.split(" ")
            es = [xi for xi in es if xi != '']
            if es == []:
                continue
            if is_number(es[0]):
                xs.append(es)

        final = [[xs[g][0],float(fs[g][0])*-1,float(fs[g][1])*-1] for g in range(0,len(xs))]

        df = pd.DataFrame(data=np.array(final),columns=["Selection Coefficient","Early Objective","Late Objective"])
        df.to_csv("result_cleaned/"+x+"_cleaned.csv")

def view_result(nm):
    df = pd.read_csv("result_cleaned/" + str(nm) + ".out_cleaned.csv")
    print(df)
    df.plot.scatter(x="Early Objective", y="Late Objective", c="Selection Coefficient",s=3)
    plt.show(block=True)

view_result(417248)



