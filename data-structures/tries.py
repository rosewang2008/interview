# tries: prefix trees 
# n-ary tree, node: characters
# each path: word
# * nodes: indicate complete words
	# TerminatingTrieNode: inherits from TrieNode

import string 
class TrieNode:
	def __init__(self):
		self.children = [None] * 26 #initializing a spot for each (lowercase) letter
		self.isLeaf = False # boolean for leaf

class Trie:
	def __init__(self):
		self.root = self.getNode()
	def getNode(self):
		return TrieNode()
	def insert(self, word):
		start = self.root
		for level in range(len(word)):
			index = string.lowercase.index(word[level])
			if not start.children[index]: # if not None = if not present
				start.children[index] = self.getNode()
			start = start.children[index]
		start.isLeaf = True
	def search(self, word):
		start = self.root
		for level in range(len(word)):
			index = string.lowercase.index(word[level])
			if not start.children[index]:
				return False
			start = start.children[index]
		return True

T = Trie()
T.insert('stan')
print(T.search('stan'))
