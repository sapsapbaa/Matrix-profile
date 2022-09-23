#This file will make your data to matrix profile

from contextlib import nullcontext
import csv
import stumpy
import plotly.express as px
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

#global variable
approx_P = []
dataframe = nullcontext
analytic_motif = []
window_size = 20 #default
threshold = 7 #set default peak threshold here

#intersect array function
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#webpage
def init(filepath,data_col):
    #import data set 
    global approx_P,dataframe,analytic_motif,window_size
    # header = ['drum pressure','excess oxygen','water level','steam flow']
    dataframe = pd.read_csv(filepath) #, names = header)
    
    #find motif by stumpy
    float_dataframe = dataframe[data_col].astype(np. float)
    approx = stumpy.scrump(float_dataframe, window_size, percentage=0.01, pre_scrump=True, s=None)
    for k in range(4): #do estimate for 4 time
        approx.update()
    approx_P = approx.P_ #get approximate value
    #print("matrix profile value:",approx_P)
    motif_idx = np.argsort(approx_P)
    #print("index where motif is ",motif_idx)
    peaks,height= find_peaks(-approx_P,height=(-threshold,0),distance=window_size)
    #print("filtered peaks ",peaks,height)
    analytic_motif = intersection(motif_idx,peaks)
    #print("actual motif index",analytic_motif)
    

def getMatrixprofile():  
    return approx_P

def getDataframe():  
    return dataframe

def getMotif():  
    return analytic_motif

def getWindowsize():
    return window_size

def setWindowsize(m):
    global window_size
    window_size = m

def setAnalyticData(data):
    global data_col
    data_col = data
    
def setPath(csv_path):
    global filepath
    filepath = csv_path

def setThreshold(th):
    global threshold
    threshold = th