# Set up program data
NumBills = 160
Amount = 1760.0
Denom1 = 10.0
Denom2 = 50.0
HaveSolution = False

# Iterate through first denomination ($10)
for i in range(1, int(Amount / Denom1), 1):

    # Iterate through second denomination ($50)
    for j in range(1, int(Amount / Denom2), 1):

        # Exceeded the number of bills?
        if i + j > NumBills:
            break

        # Found a solution?
        interim = (float(i) * Denom1) + (float(j) * Denom2)
        if interim == Amount:
            HaveSolution = True
            break

    if HaveSolution:
        break

# Solution found?
if HaveSolution:
    print("There are", i, "$", int(Denom1), "bills")
    print("There are", j, "$", int(Denom2), "bills")
    print("Totaling: $", round((float(i) * Denom1) + (float(j) * Denom2), 2))

if not HaveSolution:
    print("Something's up... did not find a solution")
