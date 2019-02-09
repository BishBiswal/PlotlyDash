import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

trace1 = go.Bar(
    x=['Kohli', 'Rahane', 'Pujara'],
    y=[102, 68, 23],
    name='1st Innings'
)
trace2 = go.Bar(
    x=['Kohli', 'Rahane', 'Pujara'],
    y=[49, 66, 141],
    name='2nd Innings'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stacked-bar.html')
