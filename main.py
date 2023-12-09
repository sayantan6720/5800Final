from CheapestFlighSearcher import CheapestFlightSearcher
from adjacencymatrix import AdjacencyMatrix

matrix = AdjacencyMatrix("Flight Data - Sheet1.csv")
airport_code_to_index_dict = {flight_label: index for index, flight_label in enumerate(matrix.get_vertices())}
searcher = CheapestFlightSearcher(matrix.get_matrix(), airport_code_to_index_dict)
print(searcher.search('JFK', 'BOS'))
