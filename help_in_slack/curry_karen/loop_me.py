# Set up a data structure which is a list of dicts or dictionaries (sometimes called a 'map' in other languages)
# Assumptions:
#   1) height is in centimeters
#   2) weight is in kilograms
person_data = [
    {'name': 'John',
    'height': 184.0,
    'weight': 84.5},
    {'name': 'Ryan',
    'height': 177.0,
    'weight': 81.8},
    {'name': 'Bobby',
    'height': 188.0,
    'weight': 92.2}
]

# "Iterate" or loop through the list above
for person in person_data:
    # Calculate the person's height in meters squared
    height_squared = (person['height']/100.0)**2
    bmi = person['weight'] / height_squared

    # Print out the person's BMI
    print("----------")
    print(person['name'], "'s BMI is: ", bmi)