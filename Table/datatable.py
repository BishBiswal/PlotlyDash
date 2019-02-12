import plotly.graph_objs as go
import plotly.offline as pyo

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace]
pyo.plot(data, filename = 'basic_table.html')
