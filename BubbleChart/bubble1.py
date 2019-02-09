import plotly.offline as pyo
import plotly.graph_objs as go

import pandas as pd
df=pd.read_csv('C:\\Users\\biswa\\plotlyDashboard\\PlotlyDash\\Data\\productsell.csv')

data = [go.Scatter(          # start with a normal scatter plot
    x=df['productCount'],
    y=df['sales'],
    text=df['profit'],
    mode='markers',
    marker=dict(size=1.5*df['profit']) # set the marker size
)]

layout = go.Layout(
    title='product count vs. Sales',
    xaxis = dict(title = 'product_count'), # x-axis label
    yaxis = dict(title = 'Sales'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
