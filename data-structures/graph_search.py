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
# graph search
# DEPTH	FIRST SEARCH (DFS): exploring each branch, going DEEP!
	# visiting every node
	# e.g. pre-order, other tree traversals
	# should check if node has already been visited
	def search(self, Node):
		# initialize some kind of list to keep track of paths 
		# check if exists
		# then:
		if Node.visited == True:
			return
		else: 
			Node.visited = True
			for neighbor in Node.connections.keys():
				search(neighbor)
			return Node.ID
a = Node('a', 5)
b = Node('b', 4)
c = Node('c', 4)
a.connect(b)
a.connect(c)
# print(a.getConnections())
# print(a.connections)
G = Graph()
G.add(a)
print(search(a))

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





