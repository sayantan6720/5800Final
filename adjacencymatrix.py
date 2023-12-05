import pandas as pd
import numpy as np


class AdjacencyMatrix:

    def __init__(self, csvPath):
        # Read CSV file
        self.flightCSV = pd.read_csv(csvPath)

        # get all airports (will be same in the manual data but going thru both lists will be
        # beneficial for future api implementations
        self.airports = []
        for airport in self.flightCSV["Airport Origin"]:
            if airport not in self.airports:
                self.airports.append(airport)

        for airport in self.flightCSV["Airport Destination"]:
            if airport not in self.airports:
                self.airports.append(airport)

        # create the adjacency matrix using numpy
        self.adjacency_matrix = np.zeros((len(self.airports), len(self.airports)))

        # helper function that gets the index of an airport from the airports list
        def get_index(airport_code):
            return self.airports.index(airport_code)

        # this loop actually fills the matrix with data
        for index, row in self.flightCSV.iterrows():
            # basically, the idea here is to get the index inside the airports list I made of both the origin (i)
            # and destination airports (j), which will act as the [i][j] to locate the correct cell
            # get the origin airport as an index on the adjacency matrix, the value of which will be the cost
            origin = get_index(row['Airport Origin'])

            # get the destination airport as an index
            destination = get_index(row['Airport Destination'])

            # get the cost of that directed edge
            cost = row['Cost']

            # fill the cell of the adjacency matrix that corresponds to that u,v edge cost
            self.adjacency_matrix[origin][destination] = cost

    def get_matrix(self):
        return self.adjacency_matrix

    def get_vertices(self):
        return self.airports


test = AdjacencyMatrix("Flight Data - Sheet1.csv")

