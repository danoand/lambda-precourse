# Set up program data
Mpg = 20
WeeklyGasPrice = [3.52, 3.57]
DrivingData = [
    {
        'num_passengers': 23,
        'avg_fare': 29.0,
        'num_miles': 160.0
    },
    {
        'num_passengers': 17,
        'avg_fare': 30.0,
        'num_miles': 220.0
    }
]

# Define program functions
def revenue(passengers, averagefare):
    return float(passengers)*averagefare

def cost(miles, mpg, price):
    return (miles / mpg) * price

# Determine the total profit
TotalProfit = 0
AvgProfitWeekAmt = 0
AvgProfitWeekId  = 0
for i in range(0, len(DrivingData)-1):
    rv = revenue(
        DrivingData[i]['num_passengers'],
        DrivingData[i]['avg_fare'])

    cst = cost(
        DrivingData[i]['num_miles'],
        Mpg,
        WeeklyGasPrice[i])

    ThisWeeksProfit = rv - cst
    ThisWeeksAvgProfit = ThisWeeksProfit / float(DrivingData[i]['num_passengers'])
    if ThisWeeksAvgProfit > AvgProfitWeekAmt:
        AvgProfitWeekAmt = ThisWeeksAvgProfit
        AvgProfitWeekId = i
    TotalProfit = TotalProfit + ThisWeeksProfit

# Print out results
print("What is their total profit over both weeks?") 
print("$", TotalProfit)
print("\nDuring which week was their average (mean) profit per passenger higher?") 
print("Week #:", AvgProfitWeekId+1)