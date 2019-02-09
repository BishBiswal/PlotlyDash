import plotly.graph_objs as go
import plotly.offline as pyo

import pandas as pd
df=pd.read_csv('C:\\Users\\biswa\\plotlyDashboard\\PlotlyDash\\Data\\bowlingpitch.csv')
random_x = df['width']
random_y =df['length']
print (random_x)
print (random_y)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = dict(      # change the marker style
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    )
)]
layout = go.Layout(
    title = 'Bowling pitch Scatterplot', # Graph title
    xaxis = dict(title = 'Blowling width',range=[-3.05, 3.05]), # x-axis label
    yaxis = dict(title = 'Bowling length',range=[0, 20.12]), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter3.html')
