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
		self.visited = False

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

#This is going to be a directed graph
class Vertex:
	def __init__(self, id):
		self.id = id
		self.visited = False

class Matrix(Vertex):
	def __init__(self):
		self.vertices = []
		self.matrix = []

	def size(self):
		return len(self.vertices)

	def add(self, Vertex):
		self.matrix.append([0]*self.size())
		self.vertices.append(Vertex.id) # in chronological order (time of insertion)
		for vertex in self.matrix:
			vertex.append(0)

	def connect(self, vertex1, vertex2): #vertex1, vertex2 not yet initialized as class Vertex
		v1 = Vertex(vertex1)
		v2 = Vertex(vertex2)
		self.add(v1)
		index1 = self.size() - 1 
		self.add(v2)
		index2 = self.size() - 1 
		self.matrix[index1][index2] = 1 

new = Vertex(1)
new1 = Vertex(2)
new2 = Vertex(3)
M = Matrix()
M.add(new)
M.add(new1)
M.add(new2)
print(M.size())
print(M.matrix)
print(M.vertices)
M.connect(4, 5)
print(M.matrix)


# graph search
# DEPTH	FIRST SEARCH (DFS): exploring each branch, going DEEP!
	# visiting every node
	# e.g. pre-order, other tree traversals
	# should check if node has already been visited
def search(Node):
	# initialize some kind of list to keep track of paths 
	# check if exists
	# then:

	if Node.visited == true:
		return
	else: 
		Node.visited = true
		for neighbor in Node.connections.keys():
			search(neighbor)

# BREADTH FIRST SEARCH (BFS): exploring each neighbor, going WIDE! 
	# finding shortest path
	# not recursive, uses QUEUES! (woo, applying knowledge)

class Queue:
	def __init__(self):
		self.queue = []
		self.count = 0
	def size(self):
		return len(self.queue)
	def add(self, item):
		self.queue.append(item)
	def delFirst(self):
		self.queue = self.queue[1:]





