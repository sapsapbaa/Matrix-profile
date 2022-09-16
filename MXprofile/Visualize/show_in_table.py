import plotly.graph_objects as go

# Create random data with numpy
import pandas as pd
import numpy as np

df = pd.read_csv('/home/phuphu/PywebIO/dataset/stable/stable_1.csv')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.timestamp,df.acc_x, df.acc_y, df.acc_z],
               fill_color='lavender',
               align='left'))
])

fig.show()