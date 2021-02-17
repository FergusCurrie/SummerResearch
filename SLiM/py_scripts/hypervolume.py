from pymoo.factory import get_performance_indicator
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def find_hyper(code):
    # Find nader point
    hyper = [10000,111110]
    for x in os.listdir('../data/result_cleaned/'):
        df = pd.read_csv('../data/result_cleaned/'+x)

        # Convert to float
        for i, row in df.iterrows():
            row['Early Objective'] = float(row['Early Objective'])
            row['Late Objective'] = float(row['Early Objective'])

        # Normalise
        for i,row in df.iterrows():
            row['Early Objective'] = (row['Early Objective'] - df['Early Objective'].min()) / (df['Early Objective'].max() - df['Early Objective'].min())
            row['Late Objective'] = (row['Late Objective'] - df['Late Objective'].min()) / (df['Late Objective'].max() - df['Late Objective'].min())

        # Find nadir point
        for i,row in df.iterrows():
            if float(row["Early Objective"]) < hyper[0]:
                hyper[0] = float(row["Early Objective"])
            if float(row["Late Objective"]) < hyper[1]:
                hyper[1] = float(row["Late Objective"])

    # Get dict of name -> hyper, normalised
    di = {}
    for x in os.listdir('../data/result_cleaned/'):
        df = pd.read_csv('../data/result_cleaned/'+x)

        # Convert to float
        for i, row in df.iterrows():
            row['Early Objective'] = float(row['Early Objective'])
            row['Late Objective'] = float(row['Early Objective'])

            # Normalise
        for i, row in df.iterrows():
            row['Early Objective'] = (row['Early Objective'] - df['Early Objective'].min()) / (df['Early Objective'].max() - df['Early Objective'].min())
            row['Late Objective'] = (row['Late Objective'] - df['Late Objective'].min()) / (df['Late Objective'].max() - df['Late Objective'].min())

        data = []
        for i,row in df.iterrows():
            data.append([-float(row["Early Objective"]), -float(row["Late Objective"])])
        A = np.array(data)

        #print(A)


        hv = get_performance_indicator("hv", ref_point=np.array([-1,-1]))
        #print("hv", hv.calc(A))
        di[x] = hv.calc(A)

    l = []
    for key in di:
       l.append(di[key])

    l.sort(reverse=True)

    l = (l[:5])
    best_solutions = []
    for x in l:
        for key in di:
            if di[key] == x:
                best_solutions.append(key)

    return best_solutions

def vr(nm):
    df = pd.read_csv("../data/result_cleaned/"+nm)
    title = ""
    for x in nm:
        if x.isnumeric():
            title += x


    #df.plot.scatter(x="Early Objective", y="Late Objective", c="Selection Coefficient",s=5,title=title,xlim=(emin,emax),ylim=(lmin,lmax))
    df.plot.scatter(x="Early Objective", y="Late Objective", c="Selection Coefficient", s=5, title=title)

    # Zoom
    if False:
        ax3 = plt.subplot(222)
        ax3.margins(x=0, y=-0.25)  # Values in (-0.5, 0.0) zooms in to center
        ax3.plot(df)
        ax3.set_title('Zoomed in')

    plt.show(block=True)



bs = find_hyper(437888)
print(bs[:5])
for x in bs[:1]:
    vr(x)