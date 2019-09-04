# Specify imports
from functools import reduce
import pandas as pd

# Fetch the data
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv")

# Define the target data
data = [
    {'column': 'RH', 'discrete': True},
    {'column': 'temp', 'discrete': False},
    {'column': 'wind', 'discrete': False}
]

def meanMedianMode(column, isDiscrete):
    # Define working objects
    wrkMap = {}

    # lstAdd returns the addition of two variables
    def lstAdd(x, y):
        return x + y

    # lstOrd returns a list of ordered elements in ascending order
    def lstOrd(x, y):
        insert = False
        rtList = []

        if not isinstance(x, list):
            if y <= x:
                return [y, x]

            return [x, y]

        if isinstance(x, list):
            for i in range(len(x)):
                if insert:
                    rtList.append(x[i])
                elif y <= x[i]:
                    rtList.append(y)
                    rtList.append(x[i])
                    insert = True
                elif y > x[i]:
                    rtList.append(x[i])

            if not insert:
                rtList.append(y)

            return rtList

    # lstMed returns the median of a list of values
    def lstMed(lst):

        if len(lst) == 1:
            return lst[0]

        if len(lst) % 2 == 0:
            # even number of elements
            i = int(len(lst)/2) - 1
            j = i + 1
            return (lst[i] + lst[j]) / 2

        return lst[int(len(lst) / 2)]

    # tallyMode tallies the number of instances of a value using a working "map"
    def tallyMode(x, y):

        if len(wrkMap) == 0:
            wrkMap[x] = 1
            wrkMap[y] = 1
        else:
            if y in wrkMap:
                wrkMap[y] = wrkMap[y] + 1
            else:
                wrkMap[y] = 1

    def getMode(mapp):
        chkVal = None
        rtVal = 0
        frstIter = True
        noMode = True

        # Set contains one one or multiple elements of the same value
        if len(mapp) == 1:
            return "no mode"

        # Determine if all values in the set occur the same number of times
        # (e.g. "a": 3 times, "b": 3 times, "c": 3 times => 'no mode')
        for key, value in mapp.items():
            if frstIter:
                chkVal = value
                frstIter = False
                continue

            if value != chkVal:
                noMode = False
                break

        if noMode:
            return "no mode"

        for value in mapp.values():
            if value > rtVal:
                rtVal = value

        tmpLst = []
        for key, value in mapp.items():
            if value == rtVal:
                tmpLst.append(key)

        if len(tmpLst) == 1:
            return tmpLst[0]

        return tmpLst

    avg = reduce(lstAdd, df[column]) / len(df[column])
    med = lstMed(reduce(lstOrd, df[column]))
    mde = 'no mode calculated'
    if isDiscrete:
        reduce(tallyMode, df[column])
        mde = getMode(wrkMap)

    return {
        'mean': avg,
        'median': med,
        'mode': mde
    }

# Iterate through the data directives
for drt in data:
    rtval = meanMedianMode(drt['column'], drt['discrete'])
    print(drt['column'], 
      'median:', 
      round(rtval['median'], 1), 
      'mean:', 
      round(rtval['mean'], 1),
      'mode:',
      rtval['mode'])