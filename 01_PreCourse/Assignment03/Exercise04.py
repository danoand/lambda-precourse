# Specify imports
import statistics as stat
import pandas as pd
from random import choice 
from tabulate import tabulate

# Fetch the data
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv")

# Define variables to house the randomly selected attribute values
varRH = []
varTemp = []
varWind = []

# Iterate to generate the desired number of data elements
for i in range(1, 10*len(df['RH'])):
    # randomly select an RH, temp, and wind value
    varRH.append(choice(df['RH']))
    varTemp.append(choice(df['temp']))
    varWind.append(choice(df['wind']))

# Construct a table of results
prtList = []
prtList.append([stat.median(varRH), stat.mean(varRH), stat.mode(varRH)])
prtList.append([stat.median(varTemp), stat.mean(varTemp), "no mode calculated"])
prtList.append([stat.median(varWind), stat.mean(varWind), "no mode calculated"])

# Print the results in tabular form
print(tabulate(prtList, headers=['column', 'median', 'mean', 'mode']))
