__author__ = 'DavidKMYang'
#https://plot.ly/python/getting-started

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import scipy
import os
import scipy.io
import numpy as np
import plotly.plotly as py
import glob
import pandas as pd
from numpy import genfromtxt
from mpl_toolkits.basemap import shiftgrid
from compiler.ast import flatten

def decile_find(lat, long):

    path_wbgt = '/Users/DavidKMYang/WBGT/ncep_tasmax_nh/'

    path_wbgt_model = '/Users/DavidKMYang/WBGT/gfdl_tasmax_nh/'

    os.chdir(path_wbgt)

    file_names_wbgt = glob.glob("*.mat")

    os.chdir(path_wbgt_model)

    file_names_wbgt_model = (glob.glob("*.mat"))[:len(file_names_wbgt)]

    totalDays = 0
    actualTotalDays = 0
    Val2D = []
    Val2D_model = []
    Val2D = np.array(Val2D)
    Val2D_model = np.array(Val2D_model)

    for n in range(len(file_names_wbgt_model)):

        tempData_wbgt = scipy.io.loadmat(path_wbgt + file_names_wbgt[n])
        tempData_wbgt = tempData_wbgt[file_names_wbgt[n][:-4]][0]
        tempData_Val_wbgt = tempData_wbgt[2]

        tempData_wbgt_model = scipy.io.loadmat(path_wbgt_model + file_names_wbgt_model[n])
        tempData_wbgt_model = tempData_wbgt_model[file_names_wbgt_model[n][:-4]][0]
        tempData_Val_wbgt_model = tempData_wbgt_model[2]


        actualTotalDays += len(tempData_Val_wbgt[0][0])

        Val2D = np.append(Val2D, np.array(tempData_Val_wbgt[lat][long]))
        Val2D_model = np.append(Val2D_model, np.array(tempData_Val_wbgt_model[lat][long]))

        Val2D = Val2D.flatten()
        Val2D_model = Val2D_model.flatten()

    flat_product = flatten(Val2D)
    flat_product_model = flatten(Val2D_model)

    flat_product.sort()
    flat_product_model.sort()

    list_hist = []
    list_model = []

    avg_hist = []
    avge_model = []
    tempVal = 0
    j=1
    curr_ind = 0

    for i in range(10):
        list_hist.append(np.percentile(flat_product, (i+1)*10))
        list_model.append(np.percentile(flat_product_model, (i+1)*10))

    for i in range(len(flat_product)):
        if flat_product[i] < list_hist[j]:
            tempVal += flat_product[i]
            curr_ind += 1
        else:
            avg_hist.append(tempVal/curr_ind)
            curr_ind = 0
            tempVal = 0
            j += 1

    tempVal = 0
    j = 1
    curr_ind = 0

    for i in range(len(flat_product_model)):
        if flat_product_model[i] < list_model[j]:
            tempVal += flat_product_model[i]
            curr_ind += 1
        else:
            avge_model.append(tempVal/curr_ind)
            curr_ind = 0
            tempVal = 0
            j += 1

    # final = np.array([(list_hist), (avg_hist), (list_model), (avge_model)])

    # final.astype(float)
    # final = np.transpose(final)
    # print final
    # final = final[1:len(final   )-1]
    # for i in range(len(final)):
    # final = str(final)
    # final = final[1:len(final)-1]
    # print final

    # latStr = str(lat)
    # latStr = latStr[1:len(latStr)-1]

    print avg_hist
    print avge_model

    # np.savetxt("/Users/DavidKMYang/WBGT/BiasCorrectionsDeciles/Deciles_" + str(lat) + "_" + str(long) + ".csv", final, delimiter = ",", fmt="%s", comments='')


# print hist_plot(14, 14)

path_wbgt = '/Users/DavidKMYang/WBGT/ncep_tasmax_nh/'
os.chdir(path_wbgt)
file_names_wbgt = glob.glob("*.mat")
tempData_wbgt = scipy.io.loadmat(path_wbgt + file_names_wbgt[0])
tempData_wbgt = tempData_wbgt[file_names_wbgt[0][:-4]][0]
# tempData_Val_wbgt = tempData_wbgt[2]

# print len(tempData_wbgt[0][0])

for i in range(18):
    for j in range(180):
        print i
        decile_find(i, j)
