import plotly.graph_objects as go

# Create random data with numpy
import pandas as pd
import numpy as np

animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
# fig.update_layout(barmode='group')

fig.show()