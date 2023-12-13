from CheapestFlightSearcher import CheapestFlightSearcher
from adjacencymatrix import AdjacencyMatrix



if __name__ == "__main__":
    matrix = AdjacencyMatrix("Flight Data - Sheet1.csv")
    airport_code_to_index_dict = {flight_label: index for index, flight_label in enumerate(matrix.get_vertices())}
    searcher = CheapestFlightSearcher(matrix.get_USD_matrix(), airport_code_to_index_dict)
    print(searcher.search('CLT', 'LAX'))