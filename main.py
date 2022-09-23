#to modify your plotly
#do it in this file

from plotly.subplots import make_subplots
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table
#import matplotlib.pyplot as plt
import pywebio
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import webpy_timeseries as ts

def page():
    Path = 'C:/Users/Thanaluk/Documents/MXprofile/dataset/move/move_1.csv'
    ts.setWindowsize(20)
    ts.init(Path,'acc_x')
    steam_df = ts.getDataframe()
    approx_P = ts.getMatrixprofile()
    analytic_motif = ts.getMotif()
    m = ts.getWindowsize()
    print(steam_df)
    #print(approx_P)

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    fig.add_trace(go.Scatter(x=steam_df.index, y= steam_df[steam_df.columns[1]].values, name = steam_df.columns[1],mode = 'lines'), row=2 ,col=1) #raw data
    fig.add_trace(go.Scatter(x=steam_df.index, y= approx_P, name = "Matrix Profile",mode = 'lines'), row=1 ,col=1) # matrix profile
    for idx in range(len(analytic_motif)):
        fig.add_vrect(x0=analytic_motif[idx], x1=analytic_motif[idx]+m,fillcolor="LightSalmon", opacity=0.5,layer="below", line_width=0,row=2 ,col=1)
        fig.add_vline(x=analytic_motif[idx], line_width=1, line_dash="dash", line_color="green",row=1,col=1)
    html = fig.to_html(include_plotlyjs="require", full_html=False)
    put_html(html)


if __name__ == '__main__':
    pywebio.start_server(page, port=80) #your local default port is 80