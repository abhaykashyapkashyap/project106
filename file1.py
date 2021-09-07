import csv
import plotly.express as px
import numpy as np
def getDataSource(data_path):
    percentage=[]
    present=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            percentage.append(float(row["Percentage"]))
            present.append(float(row["Present"]))
    return {"x":percentage,"y":present}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between days and percentage:",correlation[0,1])
def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()