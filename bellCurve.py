import plotly.figure_factory as pe
import pandas as pd
import csv

df = pd.read_csv("data.csv")

graph = pe.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist= False)
graph.show()