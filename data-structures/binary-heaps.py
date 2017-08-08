# Binary heaps (min-heaps, max-heaps)
# complete binary treee

# MIN-HEAP:
	# each node smaller than it children
	# root = min element
	# key operations:
		# insert
		# extract min

# 0 -> 1,2 				2^(n+1) - 1, 2^(n+1)
# 1 -> 3,4				
class Heap:
	def __init__(self):
		self.keys = []

	def insert(self, key):
		self.keys.append(key)
		self.swap()

	def size(self):
		return len(self.keys)

	def swap(self):
		counter = self.size() 
		while counter//2 > 0:
			if self.keys[counter-1] < self.keys[(counter-1)//2]:
				old = self.keys[(counter-1)//2]
				self.keys[(counter-1)//2] = self.keys[counter-1]
				self.keys[counter-1] = old
			counter = counter // 2
	def del_min(self):
		self.keys[0] = self.keys[self.size()-1]
		self.trickle_down()
		
	def trickle_down(self):

H = Heap()
H.insert(5)
H.insert(1)
H.insert(11)
H.insert(8)
H.insert(3)
print(H.keys)
print(H.size())