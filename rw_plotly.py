from random_walk import RandomWalk
import plotly.graph_objects as go
import plotly.io as pio


leaf = RandomWalk()
leaf.fill_walk()

# plotly code
go.Figure(data=go.Scatter(x=leaf.x_val, y=leaf.y_val, mode='markers')).show()
