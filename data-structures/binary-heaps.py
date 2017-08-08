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
		# careful of indices
		while counter//2 > 0:
			if self.keys[counter-1] < self.keys[(counter-1)//2]:
				old = self.keys[(counter-1)//2]
				self.keys[(counter-1)//2] = self.keys[counter-1]
				self.keys[counter-1] = old
			counter = counter // 2

	def del_min(self):
		self.keys[0] = self.keys[self.size()-1]
		self.keys.pop()
		print(H.keys)
		self.trickle_down()

	def trickle_down(self):
		counter = 0
		#index problem
		while (2*counter+2) in range(self.size()):
			if self.keys[2*counter + 1] > self.keys[2*counter + 2]:
				byebye = self.keys[counter]
				self.keys[counter] = self.keys[2*counter+2]
				self.keys[2*counter+2] = byebye
				counter = 2 * counter + 2
			elif self.keys[2*counter + 1] < self.keys[2*counter + 2]:
				byebye = self.keys[counter]
				self.keys[counter] = self.keys[2*counter+1]
				self.keys[2*counter+1] = byebye
				counter = 2 * counter + 1
		

H = Heap()
H.insert(5)
H.insert(1)
H.insert(11)
H.insert(8)
H.insert(3)
print(H.keys)
print(H.size())
H.del_min()
print(H.keys)