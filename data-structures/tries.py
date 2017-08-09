# tries: prefix trees 
# n-ary tree, node: characters
# each path: word
# * nodes: indicate complete words
	# TerminatingTrieNode: inherits from TrieNode

import string 
# empty root
# how to indicate which path to take?
class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isLeaf = False

class Trie:
	def __init__(self):
		self.root = self.getNode()
	def getNode(self):
		return TrieNode()
	def insert(self, word):
		# check if word exists in Trie
		# Otherwise insert
		start = self.root
		length = len(word)
		for level in range(length):
			index = string.lowercase.index(word[level])
			if not start.children[index]: # not present
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
