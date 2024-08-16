from GraphV2 import *


""" g = Graph()
edges = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6), (3, 7), (3,8),
    (4, 8), (4, 9),
    (5, 10), (5, 11),
    (6, 12), (6, 13),
    (7, 14), (7, 15), (12, 4)
] """

# Creiamo un grafo con 15 vertici e 17 archi
g = Graph()

# Aggiungiamo gli archi al grafo
""" edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'), ('C', 'H'),
    ('D', 'H'), ('D', 'I'),
    ('E', 'J'), ('E', 'K'),
    ('F', 'L'), ('F', 'M'),
    ('G', 'N'), ('G', 'O'), ('L', 'D'),  ('K', 'A') #('O', 'A'),
]

g.add_edges_from(edges)
g.printDFStree()
g.printComponentiDFS()
g.printLowpoint()
g.ordinaLowpoint()  """

"""

g6 = Graph()
edges = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6), (3, 7), (3,8),
    (4, 8), (4, 9),
    (5, 10), (5, 11),
    (6, 12), (6, 13),
    (7, 14), (7, 15), (12, 4), (15,1), (11, 1)
]
g6.add_edges_from(edges)
g6.printDFStree()
g6.printComponentiDFS()
g6.printLowpoint() 
g6.ordinaLowpoint() """

g6 = Graph()
edges = [
    (0, 1), (0, 2),
    (1, 2), (2, 3),
    (2, 4), (2, 6), (3,4),
    (3, 5), (4, 5),
    (4, 6), (5, 6)
]
g6.add_edges_from(edges)
g6.printDFStree()
g6.printComponentiDFS()
g6.printLowpoint() 
g6.ordinaLowpoint() 
