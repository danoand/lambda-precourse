from decimal import Decimal

# Set up program data
Mpg = 20
DrivingData = [
    {
        'week': 1,
        'num_passengers': 23,
        'avg_fare': 29.0,
        'num_miles': 160.0,
        'gas_price': 3.52
    },
    {
        'week': 2,
        'num_passengers': 17,
        'avg_fare': 30.0,
        'num_miles': 220.0,
        'gas_price': 3.57
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
WeekNum = 1
for wk in DrivingData:
    rv = revenue(
        wk['num_passengers'],
        wk['avg_fare'])

    cst = cost(
        wk['num_miles'],
        Mpg,
        wk['gas_price'])

    ThisWeeksProfit = rv - cst
    ThisWeeksAvgProfit = ThisWeeksProfit / float(wk['num_passengers'])

    if ThisWeeksAvgProfit > AvgProfitWeekAmt:
        AvgProfitWeekAmt = ThisWeeksAvgProfit
        AvgProfitWeekId = WeekNum
    TotalProfit = TotalProfit + ThisWeeksProfit

    WeekNum = WeekNum + 1

# Print out results

print("What is their total profit over both weeks?") 
print("$", round(TotalProfit, 2))
print("\nDuring which week was their average (mean) profit per passenger higher?") 
print("Week #:", AvgProfitWeekId)