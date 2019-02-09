import plotly.offline as pyo
import plotly.graph_objs as go

import pandas as pd
df=pd.read_csv('C:\\Users\\biswa\\plotlyDashboard\\PlotlyDash\\Data\\orangetree.csv')
data = [go.Histogram(x=df['height'],xbins=dict(start=0,end=700,size=50))]

pyo.plot(data, filename='orangetreeheight.html')
