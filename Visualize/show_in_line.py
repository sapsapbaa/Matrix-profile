import plotly.graph_objects as go

# Create random data with numpy
import pandas as pd
import numpy as np

df = pd.read_csv('/home/phuphu/PywebIO/dataset/stable/stable_1.csv')

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=df['timestamp'], y=df['acc_x'],
                    mode='lines',
                    name='acc_x'))
fig.add_trace(go.Scatter(x=df['timestamp'], y=df['acc_y'],
                    mode='lines',
                    name='acc_y'))
fig.add_trace(go.Scatter(x=df['timestamp'], y=df['acc_z'],
                    mode='lines',
                    name='acc_z'))

fig.show()