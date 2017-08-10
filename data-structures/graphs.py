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
	def __init__(self, ID,  weight):
		self.ID = ID
		self.weight = weight
		self.connections = {}
	def connect(self, other):
		self.connections[other.ID] = [other.weight]
		return other.ID
	def getConnections(self):
		return self.connections.keys()

class Graph(Node):
	def __init__(self):
		self.nodes = {}
		self.size = len(self.nodes)

	def add(self, Node):
		''' Node is already initialized. 
		add() adds the node into the graph, 
		along with the node's connecting vertices
		'''
		for conn in Node.connections.keys():
			if Node.ID in self.nodes.keys():
				self.nodes[Node.ID].append(conn)
			else: 
				self.nodes[Node.ID] = [conn]

	def insert(self, ID, weight):
		vertex = Node.__init__(self, ID, weight)
		self.add(vertex)

a = Node('a', 5)
b = Node('b', 4)
c = Node('c', 4)
a.connect(b)
a.connect(c)
# print(a.getConnections())
# print(a.connections)
G = Graph()
G.add(a)
print(G.nodes)


# Adjacency Matrix
# N x N boolean matrix, matrix[i][j] true = edge between vertex i and j
# UNDIRECTED: symmetric matrix

class Vertex:
	def __init__(self, id):
		self.id = id

class Matrix(Vertex):
	def __init__(self):
		self.vertices = []
		self.size = len(self.vertices)
		self.matrix = []

	def add(self, Vertex):
		self.vertices.append(Vertex.id) # in chronological order (time of insertion)
		self.matrix.append([0] * (self.size-1))
		for vertex in self.vertices:
			
