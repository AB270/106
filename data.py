import plotly.express as px
import csv

with open("data4.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Marks",y="Days Present")
    fig.show()