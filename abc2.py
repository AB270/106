import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path): 
    ice_cream_sales = [] 
    cold_drink_sales = [] 
    with open(data_path) as csv_file: 
        csv_reader = csv.DictReader(csv_file) 
        for row in csv_reader: 
            ice_cream_sales.append(float(row["Size of TV"])) 
            cold_drink_sales.append(float(row["time"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(datasource): 
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Temperature vs Ice Cream Sales :- \n--->",correlation[0,1]) 

def setup(): 
        data_path = "tv.csv" 

        datasource = getDataSource(data_path) 
        findCorrelation(datasource)


setup()
