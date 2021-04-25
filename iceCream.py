import plotly.express as px
import csv

with open("data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Temperature",y="Ice-cream Sales( â‚¹ )")
    fig.show()