import plotly.offline as pyo
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

trace = go.Table(
    header=dict(values=list(df.columns),
                fill = dict(color='#C2D4FF'),
                align = ['left'] * 5),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill = dict(color='#F5F8FF'),
               align = ['left'] * 5))

data = [trace]
pyo.plot(data, filename = 'pandas_table.html')
