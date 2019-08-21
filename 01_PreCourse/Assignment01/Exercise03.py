# Specify imports
from functools import reduce

def meanMedianMode(numbers):
    # Define working objects
    wrkMap = {}

    # Define reduce function(s)
    def lstAdd(x, y):
        return x + y

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

    def lstMed(lst):

        if len(lst) == 1:
            return lst[0]

        if len(lst) % 2 == 0:
            # even number of elements
            i = int(len(lst)/2) - 1
            j = i + 1
            return (lst[i] + lst[j]) / 2

        return lst[int(len(lst) / 2)]

    def lstMode(x, y):

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

        # Set contains one one or multiple elements of the same number
        if len(mapp) == 1:
            return "no mode"

        # All values in the set occur the same number of times
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

    avg = reduce(lstAdd, numbers) / len(numbers)
    med = lstMed(reduce(lstOrd, numbers))
    reduce(lstMode, numbers)
    mde = getMode(wrkMap)

    return {
        'mean': avg,
        'median': med,
        'mode': mde
    }

# print(meanMedianMode([13, 18, 13, 14, 13, 16, 14, 21, 13]))
print(meanMedianMode([1, 2, 3, 4]))
