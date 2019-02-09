import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


B1=[1.26, 0.34, 0.70, 1.75, 50.57, 1.55, 0.08, 0.42, 0.50, 3.20, 0.15, 0.49, 0.95, 0.24, 1.37, 0.17, 6.98, 0.10, 0.94, 0.38]
B2= [2.37, 2.16, 14.82, 1.73, 41.04, 0.23, 1.32, 2.91, 39.41, 0.11, 27.44, 4.51, 0.51, 4.50, 0.18, 14.68, 4.66, 1.30, 2.06, 1.19]

data = [
    go.Box(
        y=B1,
        name='B1Data'
    ),
    go.Box(
        y=B2,
        name='B2Data'
    )
]
layout = go.Layout(
    title = 'Comparison of B1 and B2'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box1.html')
