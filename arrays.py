# Hash table: array of linked lists and hash code function
# OR: has table with balanced binary search tree

# hash function: item -> slot names, 0 to m-1
class HashEntry:
	def __init__(key, value):
		self.key = key
		self.value = value
	def getKey():
		return self.key
	def getValue():
		return self.value

#modular hash function h(item) = item % m
# load factor 
# perfect hash function
# folding method 
# mid square method

def hash1(astring, tablesize):
	sum_ordinal = 0
	for letter in astring:
		sum_ordinal = sum_ordinal + ord(letter)
	return sum_ordinal % tablesize

# danger of anagrams ->  position of character as weight

def hash2(astring, tablesize):
	sum_ordinal = 0
	for position in range(len(astring)):
		sum_ordinal = sum_ordinal + ord(astring[position])*position
	return sum_ordinal % tablesize

# collision resolution

# open addressing: finding next open slot/address
# linear probing, quadratic probing
# - disadvantage: clustering
# chaining
# rehashing: looking for another slot after a collision

def rehash(position, tablesize):
	# some skip number: 3, size of skip: all slots must be revisited
	return (position + 3) % tablesize


class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def ordinal_calc(self, word): 
		''' calculates special ID for words
		'''
		sum_ordinal = 0
		for position in range(len(word)):
			sum_ordinal += ord(word[position])*position
		return sum_ordinal

	def hashposition(self, word):
		''' Function gives you position in self.slots of where
		a given word should be inserted.
		'''
		sum_ordinal = 0
		for position in range(len(word)):
			sum_ordinal += ord(word[position])*position
		return sum_ordinal % self.size

	def rehash(self, old_hash_value):
		''' Function is called if the previous location is 
		already filled.
		'''
		return (old_hash_value + 1) % self.size

	def put(self, data): 
		hashvalue = self.hashposition(data)
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = [self.ordinal_calc(data)]
			self.data[hashvalue] = [data]
			return `data` + ' has been put into the hash table.' 
		else:
			self.slots[hashvalue].append(self.ordinal_calc(data))
			self.data[hashvalue].append(data)

	def get(self, key): 
		start = self.hash(key, len(self.size))
		if self.slots[start] == key:
			return self.data[start] == key
		else: # slots[start] != key
			new_start = self.rehash(key, len(self.size))
			# recursive: if slots[new_start] == key, then return result

	# why would we need to create the functions below
	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)

# Instance of HashTable

H = HashTable(3)
print(H.put('cat'))
print(H.put('dog'))
print(H.data)
print(H.slots)


# ArrayList and Resizable Arrays
# ArrayList: arraylike data structure with dynamic resizing
# resizing factor
# CREATED NEW FILE IN JAVA FOR ARRAYS

