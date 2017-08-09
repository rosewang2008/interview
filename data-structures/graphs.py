# dem graphs: collection of nodes
# DIRECTED
# UNDIRECTED
# CONNECTED 
# ACYLCIC

# TWO TYPES OF REPRESENTATION

# Adjacency List
# node: stores adjacent vertices

# ID: string, weight: int
class Node:
	''' Using dictionaries for implementation
	'''
	def __init__(self, id, weight):
		self.id = name
		self.weight = weight
		self.children = {}
	def connect(self, other):
		self.children[other.id] = other.weight
	def

class Graph:
	def __init__(self):
		self.nodes = []
		self.size = len(self.nodes)

	def insert(self, vertex):
		




# Adjacency Matrix
