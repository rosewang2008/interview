class HashTable:
	def __init__(self, size):
		self.size = size
		self.data = [None] * size
		self.hash = [None] * size

	def hash(self, word):
		sum_ordinal = 0
		for letter in word:
			sum_ordinal += ord(letter)
		return sum_ordinal

	def position(self, word):
		sum_ordinal = 0
		for letter in word:
			sum_ordinal += ord(letter)
		return sum_ordinal % self.size
	
	def put(self, word):
		position = self.position(word)
		hashID = self.hash(word)
		if self.data[position] == None:
			self.data[position] = [word]
			self.hash[position] = [hashID]
		else:
			self.data[position].append(word)
			self.hash[position].append(hashID)

	def get(self, find):
		position = self.position(find)
		if find in self.data[position]:
			return True
		else:
			return False

Test = HashTable(11)
Test.put('Bob')

# check permutation
def check_permutation(string1, string2):
	''' Function checks whether strings are permutations of each other
	'''
	if len(string1) != len(string2):
		return False
	P = HashTable(5)
	for letter in string1:
		P.put(letter)
		print(H.data)
	# permutation: same letters, in a different order


