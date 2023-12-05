import pandas as pd
import numpy as np

# Read CSV file
flightCSV = pd.read_csv('Flight Data - Sheet1.csv')

# get all airports (will be same in the manual data but going thru both lists will be
# beneficial for future api implementations
airports = []
for airport in flightCSV["Airport Origin"]:
    if airport not in airports:
        airports.append(airport)

for airport in flightCSV["Airport Destination"]:
    if airport not in airports:
        airports.append(airport)

# create the adjacency matrix using numpy
adjacency_matrix = np.zeros((len(airports), len(airports)))


# helper function that gets the index of an airport from the airports list
def get_index(airport_code):
    return airports.index(airport_code)


# this loop actually fills the matrix with data
for index, row in flightCSV.iterrows():

    # basically, the idea here is to get the index inside the airports list I made of both the origin (i)
    # and destination airports (j), which will act as the [i][j] to locate the correct cell
    # get the origin airport as an index on the adjacency matrix, the value of which will be the cost
    origin = get_index(row['Airport Origin'])

    # get the destination airport as an index
    destination = get_index(row['Airport Destination'])

    # get the cost of that directed edge
    cost = row['Cost']

    # fill the cell of the adjacency matrix that corresponds to that u,v edge cost
    adjacency_matrix[origin][destination] = cost

print(adjacency_matrix)
