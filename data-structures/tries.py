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

	def insert(self, char):
		self.


class TerminatingTreeNode(TrieNode):
	def __init__(self):

