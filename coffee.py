import plotly.express as px
import csv

with open("coffee.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffee",y="sleep")
    fig.show()