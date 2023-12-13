from Model.CheapestFlightSearcher import CheapestFlightSearcher
from Model.adjacencymatrix import AdjacencyMatrix
matrix = AdjacencyMatrix("Model/Flight Data - Sheet1.csv")
airport_code_to_index_dict = {flight_label: index for index, flight_label in enumerate(matrix.get_vertices())}


if __name__ == "__main__":

    searcher = CheapestFlightSearcher(matrix.get_USD_matrix(), airport_code_to_index_dict)
    print(searcher.search('CLT', 'LAX'))
