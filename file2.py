import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))
    return {"x":coffee,"y":sleep}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between sleep and coffee:",correlation[0,1])
def setup():
    data_path="cups of coffee vs hour of sleeps.csv" 
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()